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


