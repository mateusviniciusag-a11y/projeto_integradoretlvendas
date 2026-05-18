import pandas as pd

print("Iniciando ETL...")


df = pd.read_csv("data/raw/vendas.csv")

df = df.dropna()
df['total'] = df['price'] * df['quantity']
df['order_date'] = pd.to_datetime(df['order_date'])
df['year'] = df['order_date'].dt.year
df['month'] = df['order_date'].dt.month
df = df[df['quantity'] > 0]


df.to_csv("data/processado/vendas_tratadas.csv", index=False)

print("ETL finalizado com sucesso!")