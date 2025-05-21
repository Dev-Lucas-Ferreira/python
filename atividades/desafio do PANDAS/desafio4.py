import pandas as pd

funcionarios = pd.read_excel('funcionarios.xlsx')
salarios = pd.read_excel('salarios.xlsx')
df = pd.merge(funcionarios, salarios, on='ID')
df['Salário Total'] = df['Salário Base'] + df['Bônus']
df = df.sort_values(by='Salário Total', ascending=False)
df.to_excel('relatorio_funcionarios.xlsx', index=False)
