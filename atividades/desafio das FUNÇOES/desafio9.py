def valorPagamento(valor, dias_atraso):
    if dias_atraso == 0:
        return valor
    else:
        multa = valor * 0.03  # 3% de multa
        juros = valor * 0.001 * dias_atraso  # 0,1% ao dia
        return valor + multa + juros

total_prestacoes = 0
valor_total = 0.0

while True:
    valor = float(input("Qual o valor da prestação (0 pra encerrar): "))
    if valor == 0:
        break
    dias = int(input("Digite o número de dias em atraso: "))
    valor_corrigido = valorPagamento(valor, dias)

    print(f"Valor a ser pago: R$ {valor_corrigido:.2f}\n")

    total_prestacoes += 1
    valor_total += valor_corrigido

print("\nRelatório do dia:")
print(f"Total de prestações pagas: {total_prestacoes}")
print(f"Valor total pago: R$ {valor_total}")
