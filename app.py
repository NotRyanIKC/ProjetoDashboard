import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Dashboard de Games", layout="wide")
st.title("🎮 Dashboard Analítico: Indústria de Videogames")
st.markdown("---")

@st.cache_data
def carregar_dados():

    return pd.read_csv('video_games_sales_tratado.csv')

df = carregar_dados()


st.sidebar.header("🕹️ Painel de Controle")


todos_generos = sorted(df['genre'].dropna().unique())


selecionar_tudo = st.sidebar.checkbox("Selecionar todos os Gêneros", value=False)

if selecionar_tudo:
    generos_sel = st.sidebar.multiselect("Selecione os Gêneros:", todos_generos, default=todos_generos)
else:
    generos_sel = st.sidebar.multiselect("Selecione os Gêneros:", todos_generos, default=todos_generos[:1])


ano_min = int(df['release_year'].min())
ano_max = int(df['release_year'].max())
periodo = st.sidebar.slider("Período de Lançamento:", ano_min, ano_max, (2000, ano_max))


df_filtrado = df[
    (df['genre'].isin(generos_sel)) & 
    (df['release_year'].between(periodo[0], periodo[1]))
]


m1, m2, m3 = st.columns(3)
m1.metric("Jogos no Filtro", len(df_filtrado))
m2.metric("Vendas Totais (M)", f"{df_filtrado['total_sales'].sum():.2f}")
m3.metric("Média da Crítica", f"{df_filtrado['critic_score'].mean():.1f}")

st.divider()


col1, col2 = st.columns(2)

with col1:
    st.subheader("1. 🏆 Top 10 Jogos Mais Vendidos")
    top10 = df_filtrado.nlargest(10, 'total_sales')
    fig1 = px.bar(top10, x='total_sales', y='title', orientation='h', 
                  color='total_sales', color_continuous_scale='Blues')
    fig1.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("2. 📊 Vendas por Console (Top 8)")
    vendas_console = df_filtrado.groupby('console')['total_sales'].sum().reset_index().nlargest(8, 'total_sales')
    fig2 = px.pie(vendas_console, values='total_sales', names='console', hole=0.4)
    st.plotly_chart(fig2, use_container_width=True)

st.divider()


col3, col4 = st.columns(2)

with col3:
    st.subheader("3. 🌎 Vendas Regionais por Gênero")
    regiao_df = df_filtrado.groupby('genre')[['na_sales', 'jp_sales', 'pal_sales']].sum().reset_index()
    fig3 = px.bar(regiao_df, x='genre', y=['na_sales', 'jp_sales', 'pal_sales'], barmode='group')
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader("4. 📈 Evolução de Vendas no Tempo")
    vendas_ano = df_filtrado.groupby('release_year')['total_sales'].sum().reset_index()
    fig4 = px.line(vendas_ano, x='release_year', y='total_sales', markers=True)
    st.plotly_chart(fig4, use_container_width=True)

st.divider()


st.subheader("5. 🎯 Nota da Crítica vs Sucesso Comercial")


fig5 = px.scatter(
    df_filtrado[df_filtrado['total_sales'] > 0], 
    x='critic_score', 
    y='total_sales', 
    size='total_sales', 
    color='genre', 
    hover_name='title',
    hover_data={'console': True, 'total_sales': ':.2f', 'critic_score': True},
    labels={
        'critic_score': 'Nota da Crítica', 
        'total_sales': 'Vendas (Milhões)',
        'console': 'Console'
    }
)

fig5.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))

st.plotly_chart(fig5, use_container_width=True)

