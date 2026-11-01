# Clase que representa un nodo
class Nodo:

    # Estructura de un nodo [numero][referencia]
    def __init__(self, numero):

        self.numero = numero
        self.siguiente = None
# clase que va a asministar todos los nodos de las listas enlazadas
class ListEnlazada:

    def __init__(self):
        
        self.cabeza = None
    
    #Metodo para insertar un nodo al inicio de la lista
    def Insertar_Nodo_al_Inicio(self, numero):
        
        # Crear un nuevo nodo con el numero recibido
        nuevo_nodo = Nodo(numero)

        # Comprobar si la lista esta vacia
        if (self.cabeza is None):

            # Vamos a pasar el nuevo nodo en nuestra cabeza
            self.cabeza = Nodo(numero)
            return 
        
        # Si la lista ya tenia nodos, el nuevo nodo apunta al que era la cabeza 
        nuevo_nodo.siguiente = self.cabeza

        # Actualizar nuestra cabeza para que apunte al nuevo nodo
        self.cabeza = nuevo_nodo

    # Metodo para insertar un nodo al final de la lista
    def Insertar_Nodo_al_Final(self, numero):

        # Crear el nodo con el numero que se recibe
        nuevo_nodo = Nodo(numero)

        # Comprobar si la lista esta vacia
        if (self.cabeza == None):

            # Si la lista esta vacia, el nuevo nodo sera el primero (Cabeza)
            self.cabeza = nuevo_nodo
            return
        
        # Referencia temporal al primer nodo
        actual = self.cabeza

        # Avanza mientras exista un nodo siguiente o actual siguiente
        while (actual.siguiente):

            # Mi nodo actual pasa a ser mi nodo siguiente o actual siguiente
            actual = actual.siguiente
        
        # cuando ya no hay un actual.siguiente es ahi cuando conecta al nuevo nodo
        actual.siguiente = nuevo_nodo




    # Metodo para eliminar un nodo al inicio de la lista
    def Eliminar_Nodo_al_Inicio(self):
        if self.cabeza is None:
            print("La lista está vacía, no hay elementos para eliminar al inicio.")
            return
        
        # La cabeza pasa a ser el siguiente nodo
        print(f"Eliminando al inicio el nodo con valor: {self.cabeza.numero}")
        self.cabeza = self.cabeza.siguiente

    # Metodo para eliminar un nodo al final de la lista
    def Eliminar_Nodo_al_Final(self):
        if self.cabeza is None:
            print("La lista está vacía, no hay elementos para eliminar al final.")
            return
        
        # Si la lista solo tiene un nodo
        if self.cabeza.siguiente is None:
            print(f"Eliminando al final el único nodo con valor: {self.cabeza.numero}")
            self.cabeza = None
            return

        # Si tiene más de un nodo, recorremos hasta encontrar el penúltimo
        actual = self.cabeza
        while actual.siguiente.siguiente is not None:
            actual = actual.siguiente
        
        print(f"Eliminando al final el nodo con valor: {actual.siguiente.numero}")
        # Desvinculamos el último nodo
        actual.siguiente = None




    # Metodo para imprimir nuestra lista enlazada
    def Imprimir_ListaEnlazada (self):

        actual = self.cabeza

        while (actual):

            # Con esta linea imprimimos nuestra lista sin saltos de linea
            print(actual.numero, " → ", end=" ")
            # Avanzamos al siguiente nodo y ahora ese sera el actuals
            actual = actual.siguiente

        # Sino apunta a None
        print("None")

Mi_lista = ListEnlazada()
Mi_lista.Insertar_Nodo_al_Inicio(3)
Mi_lista.Insertar_Nodo_al_Inicio(2)
Mi_lista.Insertar_Nodo_al_Inicio(1)
Mi_lista.Insertar_Nodo_al_Final(56)

print("Lista inicial:")
Mi_lista.Imprimir_ListaEnlazada()

print("\nEliminación al inicio:")
Mi_lista.Eliminar_Nodo_al_Inicio()
Mi_lista.Imprimir_ListaEnlazada()

print("\nEliminación al final:")
Mi_lista.Eliminar_Nodo_al_Final()
Mi_lista.Imprimir_ListaEnlazada()
