# Clase Nodo representa cada elemento de la lista enlazada
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Clase Lista_Enlazada administra la lista como estructura de datos
class Lista_Enlazada:

    def __init__(self):
        self.cabeza = None

    def insertar(self, valor):
        #Inserta un nuevo nodo con el valor especificado al final de la lista.
        nuevo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
    
    def buscar(self, valor):
        #Busca un valor en la lista y devuelve su posición.
        actual = self.cabeza
        posicion = 0

        while actual:
            if actual.valor == valor:
                return posicion
            actual = actual.siguiente
            posicion += 1

        return -1

    def mostrar(self):
        #Muestra todos los valores de la lista enlazada.
        actual = self.cabeza
        if actual is None:
            print("La lista está vacía.")
        else:
            print("Elementos en la lista enlazada:")
            while actual:
                print(f" - {actual.valor}")
                actual = actual.siguiente
        