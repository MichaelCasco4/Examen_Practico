#Clase que inicializa un elemento y una prioridad
class Elementos:

    def __init__(self, nombre, prioridad):
        self.nombre= nombre
        self.prioridad= prioridad
    
    def __str__(self):
        return f"{self.nombre} (Prioridad: {self.prioridad})"
    
#Clase que representa una cola de prioridad 
class ColaPrioridad:

    def __init__(self):
        #Inicializa la cola como una lista vacia
        self.elementos = []

    def encolar(self, nombre, prioridad):
        #Agrega un nuevo elemento a la cola y ordena según la prioridad
        nuevo = Elementos(nombre, prioridad)
        self.elementos.append(nuevo)
        self.ordenar_prioridad()

    def ordenar_prioridad(self):
        #Ordena la lista de elementos de menor a mayor prioridad
        for i in range(len(self.elementos)):
            for j in range(i + 1, len(self.elementos)):
                if self.elementos[j].prioridad < self.elementos[i].prioridad:
                    # Intercambia si la prioridad es menor
                    self.elementos[i], self.elementos[j] = self.elementos[j], self.elementos[i]

    def descolocar(self):
        #Elimina y devuelve el elemento con mayor prioridad (primero de la lista)
        if not self.esta_vacia(): 
            return self.elementos.pop(0) # El primer elemento es el de mayor prioridad
        return None     
    
    def esta_vacia(self):
         #Verifica si la cola está vacía. return True si no hay elementos, False en caso contrario.
         return len(self.elementos) == 0

    def mostrar(self):
        #Muestra todos los elementos de la cola en orden de prioridad.
        if self.esta_vacia():
            print("La cola esta vacia: ")
        else:
            print("Elementos een la cola (ordenados por prioridad): ")
            for elem in self.elementos:
                print(f"- {elem}")
            




        

