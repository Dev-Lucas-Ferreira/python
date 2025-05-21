import pandas as pd

df = pd.read_excel('estoque_sujo.xlsx')
df['Quantidade'] = df['Quantidade'].fillna(0)
df['Preço'] = df['Preço'].replace('R\$', '', regex=True)
df['Preço'] = df['Preço'].str.replace(',', '.').astype(float)
df['Preço'] = df['Preço'].fillna(df['Preço'].mean())
df['Categoria'] = df['Categoria'].str.strip().str.lower()
df['Categoria'] = df['Categoria'].replace({
    'eletronicos': 'Eletrônicos',
    'eletrônicos': 'Eletrônicos',
    'eletro': 'Eletrônicos',
    'alimentos': 'Alimentos',
    'alimento': 'Alimentos'
})
relatorio = df.groupby('Categoria')['Quantidade'].sum().reset_index()
df.to_excel('estoque_limpo.xlsx', index=False)
