def quantidade(numero):
    return len(str(abs(numero)))

numero = int(input("Digte um número inteiro:"))
qtd = quantidade(numero)

print(f"O numero {numero} tem essa quantidade {qtd} de digitos.")