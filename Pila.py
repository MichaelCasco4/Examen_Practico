class nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cabeza = None 
    
    def push(self,dato):
        nuevoNodo = nodo(dato)

        nuevoNodo.siguiente = self.cabeza
        self.cabeza = nuevoNodo

    def peek(self):
        if self.cabeza is None:
            return None
        temporal = self.cabeza.dato
        return temporal

    def pop(self):

        if self.cabeza is None:
            return None
        temporal = self.cabeza

        self.cabeza = self.cabeza.siguiente
        return temporal.dato
    
    def imprimir(self):
        
        if self.cabeza is None:
            return False
        
        temporal = self.cabeza

        while temporal:
            print(temporal.dato)
            temporal = temporal.siguiente

        return True
    
    def no_vacia(self):
        if self.cabeza is None:
            return False
        else:
            return True