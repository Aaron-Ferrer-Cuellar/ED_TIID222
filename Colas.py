from collections import deque
def programa_colas():
    cola = deque()
    while True:
        print("\n--- MENÚ COLAS ---")
        print("1. Insertar cola\n2. Borrar en cola\n3. Listar cola\n4. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            num = input("Número a insertar: ")
            cola.append(num)
        elif opcion == "2":
            if cola:
                print("Eliminado:", cola.popleft())
            else:
                print("Cola vacía")
        elif opcion == "3":
            print("Cola:", cola)
        elif opcion == "4":
            break

while True:
    programa_colas()
    Ejecutar = input("\n¿Ejecutar nuevamente? (s/n): ")
    
    if Ejecutar != "s":
        break