def converter_horas(horas_24, minutos):
    if horas_24 == 0:
        horas_12 = 12
        periodo = "A"
    elif 1 <= horas_24 < 12:
        horas_12 = horas_24
        periodo = "A"
    elif horas_24 == 12:
        horas_12 = 12
        periodo = "P"
    else:
        horas_12 = horas_24 - 12
        periodo = "P"
    
    return horas_12, minutos, periodo

def relogio(horas, minutos, periodo):
    sufixo = "A.M" if periodo == "A" else "P.M"
    print(f"{horas}:{minutos:02d} {sufixo}")

while True:
    hora_entrada = int(input("Digite a hora (0 a 23): "))
    minuto_entrada = int(input("Digite os minutos (0 a 59): "))

    hora_12, minuto, periodo = converter_horas(hora_entrada, minuto_entrada)
    relogio(hora_12, minuto, periodo)

    repetir = input("Deseja converter outro horário? (s/n): ").lower()
    if repetir != 's':
        print("Programa encerrado.")
        break
