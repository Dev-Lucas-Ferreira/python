import pandas as pd

dados = {"Nome":["anão","bible","traficante","claudio" ,"mecanico"], "Idade":[20,19,21,22,43]}
df = pd.DataFrame(dados)

print(df['Idade'].mean())