class Nodo:
    def __init__(self, titulo):
        self.titulo = titulo
        self.siguiente = None  # Apunta al siguiente nodo


class ListaReproduccion:
    def __init__(self):
        self.inicio = None  # Primer nodo de la lista
        self.actual = None  # Nodo actualmente en reproducción

    def existe_cancion(self, titulo):
        temp = self.inicio
        while temp:  # Recorre la lista
            if temp.titulo == titulo:  # Si encuentra coincidencia, retorna True
                return True
            temp = temp.siguiente
        return False  # No encontró la canción

    def agregar_cancion(self, titulo):
        if self.existe_cancion(titulo):  # Verifica si la canción ya existe
            print(f"La canción '{titulo}' ya existe en la lista.")
            return False

        nuevo = Nodo(titulo)
        if not self.inicio:  # Si la lista está vacía, el nuevo nodo es el primero
            self.inicio = nuevo
            self.actual = self.inicio
        else:
            temp = self.inicio
            while temp.siguiente:  # Recorre hasta el último nodo
                temp = temp.siguiente
            temp.siguiente = nuevo  # Agrega el nuevo nodo al final
        return True

    def eliminar_cancion(self, titulo):
        temp = self.inicio
        anterior = None
        while temp:  # Recorre la lista buscando el nodo a eliminar
            if temp.titulo == titulo:
                if anterior:  # Si no es el primer nodo
                    anterior.siguiente = temp.siguiente
                else:  # Si es el primer nodo
                    self.inicio = temp.siguiente

                if self.actual == temp:  # Si la canción actual es la que se elimina
                    self.actual = self.inicio
                return True
            anterior = temp
            temp = temp.siguiente
        return False  # No encontró la canción a eliminar

    def reproducir_siguiente(self):
        if self.actual and self.actual.siguiente:  # Si hay una canción siguiente
            self.actual = self.actual.siguiente
            return self.actual.titulo
        return None  # No hay siguiente canción

    def reproducir_anterior(self):
        if self.actual == self.inicio or not self.actual:  # Si no hay anterior
            return None

        temp = self.inicio
        anterior = None
        while temp != self.actual:  # Recorre hasta encontrar el nodo actual
            anterior = temp
            temp = temp.siguiente
        if anterior:  # Si encontró un nodo anterior
            self.actual = anterior
            return self.actual.titulo
        return None

    def mostrar_lista(self):
        canciones = []
        temp = self.inicio
        while temp:  # Recorre toda la lista y agrega los títulos
            canciones.append(temp.titulo)
            temp = temp.siguiente
        return canciones