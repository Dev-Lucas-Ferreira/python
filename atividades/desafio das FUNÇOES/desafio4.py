def calculos():
    Km_litro = float(input("Quantos Km por litro: "))
    distancia = float(input("Quantos km percorridos: "))
    preco_litro = 6.30

    
    def litros_gastos():
        return distancia / Km_litro

    
    def custo():
        litros = litros_gastos()
        return litros * preco_litro

    
    print(f"Serão gastos {litros_gastos():.2f} litros de combustível.")
    print(f"O custo total será de R${custo():.2f}.")


calculos()
