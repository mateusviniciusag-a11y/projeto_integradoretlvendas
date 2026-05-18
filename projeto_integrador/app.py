import streamlit as st
import pandas as pd

df = pd.read_csv("projeto_integrador/data/processado/vendas_tratadas.csv")

st.set_page_config(layout="wide")

st.title(" Dashboard de Vendas")
st.sidebar.header("Filtros")
anos = sorted(df['year'].unique())
ano = st.sidebar.selectbox("Ano", anos)
regioes = df['region'].unique()
regiao = st.sidebar.selectbox("Região", regioes)
df_filtrado = df[(df['year'] == ano) & (df['region'] == regiao)]
st.subheader("Resumo")

col1, col2 = st.columns(2)

faturamento = df_filtrado['total'].sum()
pedidos = df_filtrado['order_id'].nunique()

col1.metric("Faturamento Total", f"R$ {faturamento:.2f}")
col2.metric("Pedidos", pedidos)

st.subheader("Vendas por Categoria")
st.bar_chart(df_filtrado.groupby('category')['total'].sum())
st.subheader("Vendas por Região")
st.bar_chart(df_filtrado.groupby('region')['total'].sum())
st.subheader("Vendas ao longo do tempo")
df_time = df_filtrado.groupby('order_date')['total'].sum()
st.line_chart(df_time)
