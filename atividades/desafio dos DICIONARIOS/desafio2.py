lista_de_compras ={
    "Arroz":{
        "Quantidade":"5",
        "Preço":"15,48"
    },"\n"
    "Feijão":{
        "Quantidade":"5",
        "Preço":"17,90"
    },"\n"
    "Ovos":{
        "Quantidade":"30",
        "Preço":"25,18"
    },"\n"
    "Oléo":{
        "Quantidade":"2",
        "Preço":"12,23"
    }
}

for item, info in lista_de_compras.items():
    print(f"{item}:\n  Quantidade: {info['Quantidade']}\n  Preço: R$ {info['Preço']}\n")
