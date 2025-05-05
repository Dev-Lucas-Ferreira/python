def contagem():
    try:
        numero = int(input("Por onde a contagem deve começar? "))
        for i in range(numero, -1, -1):
            print(i)
    except ValueError:
        print("Valor inválido. Por favor, digite um número inteiro.")

contagem()
