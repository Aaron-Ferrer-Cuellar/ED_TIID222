# CAPTURA 1: Consultar elemento
numeros1 = [10, 20, 30, 40, 50]
print("Captura 1:", numeros1[2])  

# CAPTURA 2: Modificar elemento
numeros2 = [10, 20, 30, 40, 50]
numeros2[2] = 100
print("Captura 2:", numeros2) 

# CAPTURA 3: Agregar elemento con append()
numeros3 = [10, 20, 30, 40, 50]
numeros3.append(60)
print("Captura 3:", numeros3)  

# CAPTURA 4: Agregar lista con append()
numeros4 = [10, 20, 30, 40, 50]
numeros4.append([60, 70])
print("Captura 4 - Lista:", numeros4)
print("Captura 4 - Índice 5:", numeros4[5])     
print("Captura 4 - Imprimir 60:", numeros4[5][0]) 

# CAPTURA 5: Insertar con insert()
numeros5 = [10, 20, 30, 40]
numeros5.insert(2, 25)
print("Captura 5:", numeros5)  

# CAPTURA 6: Concatenación con +
numeros6 = [10, 20, 30, 40]
numeros6 = numeros6 + [50]
print("Captura 6:", numeros6)  

# CAPTURA 7: Agregar múltiples elementos (+ y extend)
numeros7_a = [10, 20, 30, 40] + [50, 60, 70]
numeros7_b = [10, 20, 30]
otros_numeros = [40, 50, 60]
numeros7_b.extend(otros_numeros)
print("Captura 7a:", numeros7_a)
print("Captura 7b - numeros:", numeros7_b)          
print("Captura 7b - otros_numeros:", otros_numeros)

# CAPTURA 8: Slicing con len()
numeros8 = [10, 20, 30]
numeros8[len(numeros8):] = [40]
print("Captura 8:", numeros8)  

# EJERCICIO 1.
# 1: Agregar 95 al final
calificaciones = [70, 85, 90, 65]
calificaciones.append(95)
print(calificaciones)

# 2: Agregar 80 entre 85 y 90
calificaciones = [70, 85, 90, 65]
calificaciones.append(95)
calificaciones.insert(2, 80)
print(calificaciones)

# 3: Imprimir arreglo completo
calificaciones = [70, 85, 90, 65]
calificaciones.append(95)
calificaciones.insert(2, 80)
print(calificaciones)


# EJERCICIO 2.
# 1: Imprimir arreglo completo de colores
colores = ["Azul", "Amarillo", "Rosa"]
colores.extend(["Verde", "Morado", "Rojo", "Negro"])
print(colores)

# 2: Imprimir únicamente "Negro"
colores = ["Azul", "Amarillo", "Rosa"]
colores.extend(["Verde", "Morado", "Rojo", "Negro"])
print(colores[6])


# EJERCICIO 3.
# 1: Imprimir arreglo completo del reto
numeros = [10, 20, 30, 40]
numeros.insert(2, 95)
numeros.extend([50, 67])
print(numeros)

# 2: Imprimir el número 95
numeros = [10, 20, 30, 40]
numeros.insert(2, 95)
numeros.extend([50, 67])
print(numeros[2])

# 3: Imprimir el número 67
numeros = [10, 20, 30, 40]
numeros.insert(2, 95)
numeros.extend([50, 67])
print(numeros[6])

# 4: Indicar qué posición ocupa cada uno
numeros = [10, 20, 30, 40]
numeros.insert(2, 95)
numeros.extend([50, 67])
print("El ", numeros[2], "esta en la posicion 2")
print("El ", numeros[5], "esta en la posicion 5")
print("El ", numeros[6], "esta en la posicion 6")