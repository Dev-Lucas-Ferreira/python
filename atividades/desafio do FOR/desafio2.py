texto = "Aurelianodominguezfernandocarlosbenjaminaristidesmarcelogustavonogueira"
letra = ["a","e","n","o"]
contador = {}


for i in letra:
    contador[i] = 0


for char in texto:
    letras = char.lower()
    if letras in contador:
        contador[letras] += 1


for i in letra:
    print(f"A letra '{i}' apareceu {contador[i]} vezes.")