def tabuada(escolha):
    def multiplicacao():
        while True:
            try:
                numero1 = int(input("Digite um número: "))
                numero2 = int(input("Digite outro número: "))
                resultado = numero1 * numero2
                print(f"O valor da multiplicação é: {resultado}")
                break
            except ValueError:
                print("Por favor, insira um número válido.")

    def adiçao():
        while True:
            try:
                numero1 = int(input("Digite um número: "))
                numero2 = int(input("Digite outro número: "))
                resultado = numero1 + numero2
                print(f"O valor da soma é: {resultado}")
                break        
            except ValueError:
                print("Por favor, insira um número válido.")

    def subtraçao():
        while True:
            try:
                numero1 = int(input("Digite um número: "))
                numero2 = int(input("Digite outro número: "))
                resultado = numero1 - numero2
                print(f"O valor da subtração é: {resultado}")
                break        
            except ValueError:
                print("Por favor, insira um número válido.")

    def tabuada_interativa():
        while True:
            try:
                numero = int(input("Digite um número para ver a tabuada (ou 0 para sair): "))
                if numero == 0:
                    print("Saindo da tabuada...\n")
                    break
                print(f"\nTabuada do {numero}:")
                for i in range(1, 11):
                    print(f"{numero} x {i} = {numero * i}")
                print()
            except ValueError:
                print("Por favor, insira um número válido.")

    if escolha == "1":
        adiçao()
    elif escolha == "2":
        subtraçao()
    elif escolha == "3":
        multiplicacao()
    elif escolha == "4":
        tabuada_interativa()
    else:
        print("Opção inválida!")

def menu():
    print("Equações simples")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Tabuada Interativa")

    try:
        escolha = input("Qual operação deseja fazer? ")
        tabuada(escolha)
    except ValueError:
        print("Por favor, insira uma opção válida.")

menu()
