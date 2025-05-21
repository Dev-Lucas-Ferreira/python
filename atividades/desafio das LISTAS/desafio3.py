numeros_repetidos = [1,2,2,3,4,4,5,6,6,7,8,8,9,]
numeros_nao_repetidos = []
for numeros in numeros_repetidos:
    if numeros not in numeros_nao_repetidos:
        numeros_nao_repetidos.append(numeros)

print(numeros_nao_repetidos)