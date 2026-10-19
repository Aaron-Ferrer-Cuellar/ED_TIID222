matriz = [
    [73, 12, 89, 34],
    [5, 61, 27, 94],
    [46, 18, 80, 3]
]

matriz.append([39, 22, 69, 17])

print(matriz[1])

for i in matriz:
    if 61 in i:
        print (f"61 encontrado en la fila {i}")
        break

for filas in matriz:
    for numeros in filas:
        print (f"3 encontrado en {filas}")
        break


cola=[]
for elemento in ['A', 'B', 'C', 'D']:
    cola.append(elemento)

numeros = [10, 20, 30, 40, 50]
numeros.append([60, 70])
print(numeros[5])