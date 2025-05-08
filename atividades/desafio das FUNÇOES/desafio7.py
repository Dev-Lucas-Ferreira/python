def somaimpostos(taxaimposto,custo):
    custoimposto = custo + (taxaimposto / 100)*custo
    return custoimposto

taxa = float(input("Qual a taxa:"))
valor = float(input("Qual o valor:"))

valor_final = somaimpostos(taxa,valor)
print(f"{valor_final}")
