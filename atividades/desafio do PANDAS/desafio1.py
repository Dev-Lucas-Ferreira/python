import pandas as pd

df = pd.read_excel('vendas.xlsx')
df['Total'] = df['Quantidade'] * df['Preço Unitário']
df['Data'] = pd.to_datetime(df['Data'])
df['AnoMes'] = df['Data'].dt.to_period('M')
vendas_mensais = df.groupby('AnoMes')['Total'].sum().reset_index()
maior_mes = vendas_mensais.loc[vendas_mensais['Total'].idxmax()]
vendas_mensais.to_excel('vendas_mensais.xlsx', index=False)
