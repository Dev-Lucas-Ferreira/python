print("==================Formulario====================")
nome_do_aluno = input("Qual é o seu nome?? ")
nota1 = float(input("Qual foi sua nota do 1°Bimestre: "))
nota2 = float(input("Qual foi sua nota do 2°Bimestre: "))
nota3 = float(input("Qual foi sua nota do 3°Bimestre: "))
nota4 = float(input("Qual foi sua nota do 4°Bimestre: "))
nota_final = (nota1 + nota2 + nota3 + nota4)/4
print("================================================")

if nota_final >= 70:
    print("{==========Notas============}")
    print(f"Nome: {nome_do_aluno}")
    print(f"1°Bimestre: {nota1}")
    print(f"2°Bimestre: {nota2}")
    print(f"3°Bimestre: {nota3}")
    print(f"4°Bimestre: {nota4}")
    print(f"Média: {nota_final}")
    print("Situação: Aprovado")
    print("{===========================}")
elif 60 <= nota_final <7:
    print("{==========Notas============}")
    print(f"Nome: {nome_do_aluno}")
    print(f"1°Bimestre: {nota1}")
    print(f"2°Bimestre: {nota2}")
    print(f"3°Bimestre: {nota3}")
    print(f"4°Bimestre: {nota4}")
    print(f"Média: {nota_final}")
    print("Situação: Recuperação")
    print("{===========================}")
else:
    print("{==========Notas============}")
    print(f"Nome: {nome_do_aluno}")
    print(f"1°Bimestre: {nota1}")
    print(f"2°Bimestre: {nota2}")
    print(f"3°Bimestre: {nota3}")
    print(f"4°Bimestre: {nota4}")
    print(f"Média: {nota_final}")
    print("Situação: Reprovado")
    print("{===========================}")