def imc():
    altura = float(input("Qual é a sua altura (em metros): "))
    peso = float(input("Qual o seu peso (em kg): "))

    calculo = peso / (altura ** 2)
    print(f"O seu IMC é: {calculo:.2f}")
    
    if calculo < 18.5:
        print("Você está abaixo do peso.")
    elif 18.5 <= calculo < 24.9:
        print("Você está com o peso normal.")
    elif 25 <= calculo < 29.9:
        print("Você está com sobrepeso.")
imc()