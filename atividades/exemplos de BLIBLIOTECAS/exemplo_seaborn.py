import seaborn as sns
import matplotlib.pyplot as plt

# Dados simples
dados = {
    "altura": [1.60, 1.70, 1.75, 1.80, 1.65],
    "peso": [55, 65, 70, 80, 60]
}

# Gráfico
sns.scatterplot(x=dados["altura"], y=dados["peso"])
plt.title("Altura x Peso")
plt.xlabel("Altura (m)")
plt.ylabel("Peso (kg)")
plt.show()
