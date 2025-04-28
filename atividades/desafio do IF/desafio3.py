peso = float(input("Qual é o seu peso? "))
altura = float(input("Qual é a sua altura? "))
imc = peso/(altura*altura)

if imc < 18.5:
    print(f"{imc}")
    print("Você está abaixo do peso")
elif 18.5 <= imc < 24.9:
    print(f"{imc}")
    print("Você está com o peso normal")
elif 25 <= imc < 29.9:
    print(f"{imc}")
    print("Você está acima do peso")
else:
    print(f"{imc}")
    print("Você está obeso") 
    