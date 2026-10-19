def programa_pilas():
    pila = ['1', '2']
    while True:
        print("\n--- MENÚ PILAS ---")
        print("1. Insertar pila\n2. Borrar en pila\n3. Listar pila\n4. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            num = input("Número a agregar: ")
            pila.append(num)
        elif opcion == "2":
            if pila:
                print("Eliminado:", pila.pop())
            else:
                print("Pila vacía")
        elif opcion == "3":
            print("Pila:", pila)
        elif opcion == "4":
            break

while True:
    programa_pilas()
    Ejecutar = input("\n¿Ejecutar nuevamente? (s/n): ")
    
    if Ejecutar != "s":
        break