numeros = [1, 2, 3, 4, 5]
quadrados = []
i = 0


while i < len(numeros):
    quadrado = numeros[i] ** 2
    quadrados.append(quadrado)
    i += 1

print(quadrados)
