class Nodo:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad
        self.siguiente = None


class ColaPrioridad:
    def __init__(self):
        self.frente = None

    def Insertar(self, nombre, prioridad):
        nuevo = Nodo(nombre, prioridad)

        if self.frente is None or prioridad < self.frente.prioridad:
            # Insertar al principio
            nuevo.siguiente = self.frente
            self.frente = nuevo
        else:
            # Buscar la posicion correcta
            actual = self.frente
            while actual.siguiente is not None and actual.siguiente.prioridad <= prioridad:
                actual = actual.siguiente

            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo

        print(f"Elemento '{nombre}' con prioridad {prioridad} insertado correctamente.")

    def Eliminar(self):
        if self.frente is None:
            print("La cola esta vacia!")
            return None
        eliminado = self.frente
        self.frente = self.frente.siguiente
        print(f"Elemento '{eliminado.nombre}' con prioridad {eliminado.prioridad} fue eliminado.")
        return eliminado.nombre

    def Imprimir(self):
        if self.frente is None:
            print("La cola esta vacia!")
        else:
            print("Contenido de la cola (de mayor a menor prioridad):")
            actual = self.frente
            while actual is not None:
                print(f"Nombre: {actual.nombre}, Prioridad: {actual.prioridad}")
                actual = actual.siguiente