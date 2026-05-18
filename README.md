# Projeto ETL - Análise de Vendas

## Objetivo
O objetivo deste projeto foi aplicar o processo de ETL (Extract, Transform, Load) em uma base de dados de vendas, e depois apresentar os resultados em um dashboard interativo.

## Fonte dos dados
Os dados utilizados foram obtidos do Kaggle.

## Processo ETL

### Extract
Foi feita a leitura de um arquivo CSV com os dados de vendas.

### Transform
Durante essa etapa, foram feitas algumas melhorias nos dados:
- Remoção de valores nulos
- Criação de uma coluna de faturamento total
- Conversão da coluna de datas
- Criação das colunas de ano e mês
- Remoção de valores inconsistentes

### Load
Após o tratamento, os dados foram salvos em um novo arquivo:
data/processado/vendas_tratadas.csv


## Dashboard

O dashboard foi desenvolvido utilizando Streamlit e permite visualizar os dados de forma interativa.

Funcionalidades:
- Filtro por ano
- Filtro por região
- Visualização do faturamento total
- Quantidade de pedidos
- Gráficos por categoria
- Evolução das vendas ao longo do tempo

## Acesso ao dashboard

O projeto pode ser acessado online pelo link:

https://projetointegradoretlvendas-dmkgbahbe2frbjiyuw5win.streamlit.app/

## Insights

- Existem diferenças de faturamento entre as regiões
- Algumas categorias vendem mais que outras
- As vendas variam ao longo do tempo

## Tecnologias utilizadas

- Python
- Pandas
- Streamlit
- GitHub
