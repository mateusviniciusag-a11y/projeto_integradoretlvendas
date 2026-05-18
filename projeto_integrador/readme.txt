Projeto ETL - Análise de Vendas

Objetivo
Realizar um processo de ETL (Extract, Transform, Load) em um dataset de vendas e apresentar os resultados em um dashboard interativo.

Fonte dos Dados
Dados obtidos da plataforma Kaggle.

ETL

Extract
Os dados foram carregados a partir de um arquivo CSV contendo informações de vendas.

Transform
Foram feitas as seguintes transformações:
- Remoção de valores nulos
- Criação da coluna de faturamento total
- Conversão da coluna de datas
- Criação de colunas de ano e mês
- Remoção de valores inválidos

Load
Os dados tratados foram armazenados em um novo arquivo CSV na pasta `processado`.

Dashboard
O dashboard foi desenvolvido utilizando Streamlit e possui:
Filtros por ano e região
Métricas de faturamento e quantidade de pedidos
Gráficos de vendas por categoria
Análise temporal das vendas

Insights
O faturamento varia entre regiões, indicando concentração de vendas
Algumas categorias apresentam maior volume de vendas
Há variação nas vendas ao longo do tempo, sugerindo padrões sazonais