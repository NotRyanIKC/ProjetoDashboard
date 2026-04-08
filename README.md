# 🎮 Dashboard Analítico: Indústria de Videogames

Este projeto consiste em uma análise de dados ponta a ponta sobre o mercado global de videogames (1980-2024). Ele abrange desde a extração e tratamento de dados brutos até a construção de um dashboard interativo em painel web.

## 📌 Sobre o Projeto
O projeto foi desenvolvido em duas etapas principais:
1. **Análise Exploratória e Tratamento de Dados (ETL):** Utilizando um *Jupyter Notebook*, os dados brutos extraídos do Kaggle passaram por um processo de limpeza e análise para identificar inconsistências, entender distribuições e exportar uma base consolidada (`video_games_sales_tratado.csv`).
2. **Dashboard Interativo:** Uma aplicação web construída com *Streamlit* e *Plotly*, que consome os dados tratados e permite ao usuário filtrar e interagir com gráficos dinâmicos para obter insights de negócios sobre o mercado de games.

## 📊 Funcionalidades do Dashboard
O painel de controle possui filtros laterais interativos (Gênero e Período de Lançamento) e apresenta as seguintes visualizações:
* **Top 10 Publishers:** Gráfico de barras horizontais destacando as publicadoras com maior volume de vendas.
* **Participação por Console:** Gráfico de rosca (pie chart) exibindo as vendas por plataforma.
* **Vendas Regionais por Gênero:** Comparativo entre as vendas na América do Norte, Japão e região PAL (Europa, etc.).
* **Evolução de Vendas no Tempo:** Gráfico de linhas mostrando o comportamento do mercado ano a ano.
* **Nota da Crítica vs Sucesso Comercial:** Gráfico de dispersão (scatter plot) relacionando a pontuação da crítica (`critic_score`) com o total de vendas.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Tratamento e Análise de Dados:** Pandas, Jupyter Notebook
* **Visualização de Dados:** Plotly (Plotly Express)
* **Criação do Dashboard Web:** Streamlit
* **Fonte de Dados:** [Kaggle - Video Game Sales and Industry Data (1980-2024)](https://www.kaggle.com/datasets/bhushandivekar/video-game-sales-and-industry-data-1980-2024)

## 📁 Estrutura do Repositório
* `Dashboard Videogames.ipynb`: Notebook contendo toda a lógica de exploração, limpeza de dados e conclusões parciais.
* `app.py`: Código-fonte principal da aplicação web (Dashboard Streamlit).
* `video_games_sales_tratado.csv`: Base de dados limpa gerada pelo notebook e consumida pelo dashboard. *(Nota: certifique-se de que este arquivo foi gerado antes de rodar o app)*.

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
Certifique-se de ter o Python instalado na sua máquina. É recomendável utilizar um ambiente virtual (venv).

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
   cd SEU_REPOSITORIO

   
