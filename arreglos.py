""" 

#Declarando un array
numeros = [10, 20, 30, 40, 50]

#Imprimo un elemento especifico 
print(numeros[2])

#Reasignacion
numeros[3] = 35
print(numeros)

#Agrega un nuevo valor al final del arreglo
numeros.append(45)
print(numeros)

#Eliminamos un valor en el arreglo
numeros.remove(35)
print(numeros)

#Eliminamos un valor del arreglo usando la posicion
numeros.pop(4)
print(numeros)

frutas = ["Manzana", "Fresa", "Sandia", "Mango", "Melon", "Platano"]
frutas.pop(4)
print(frutas)

frutas.remove("Manzana")
print(frutas)



# Declaracion de un arreglo vacio
Arrglo = [];
print(Arrglo)

n = int(input("Ingrese el tamano del arreglo: "))

for i in range(n):
    dato = int(input("Ingrese un numero para el arreglo: "))
    Arrglo.append(dato)

print(Arrglo)

Arrglo2 = [0] * n
n2 = int(input("Ingrese el tamano del arreglo: "))

for i in range(n2):
    dato2 = int(input("Ingrese un numero para el arreglo: "))
    Arrglo2[i] = dato

print(Arrglo2)

"""


Arrglo = []
Arreglo2 = []

n = int(input("Ingrese el tamano del arreglo: "))

for i in range(n):
    dato = int(input("Ingrese un numero para el arreglo: "))
    Arrglo.append(dato)

for i in range(n):
    num = Arrglo[i]
    if num % 5 == 0:
        Arreglo2.append(num)
    else:
        Arreglo2.append(num + (5 - (num % 5)))

print("Array original:", *Arrglo)
print("Array cincuerizado:", *Arreglo2)

numw = 23
print(numw % 5)

    