palleta_de_cores ={
    "vermelho":{
        "codigo":"#FF0000"
    },
    "verde":{
        "codigo":"#00FF00"
    },
    "azul":{
        "codigo":"#0000FF"
    }
}
for item, info in palleta_de_cores.items():
    print(f"{item}\n  código: {info['codigo']}")