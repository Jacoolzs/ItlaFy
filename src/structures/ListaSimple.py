from src.structures.NodoSimple import NodoSimple
class ListaSimple:

    # Complejidad: O(1)
    def __init__(self):
        self.head = None

    # Complejidad: O(n)
    def agregar(self, cancion):

        nuevaCancion = NodoSimple(cancion)

        if self.head is None:
            self.head = nuevaCancion
            return True

        actual = self.head
        while(actual.siguiente is not None):
            actual = actual.siguiente

        actual.siguiente = nuevaCancion
        return True

    # Complejidad: O(n)
    # Permite iterar sobre las canciones de la lista simple sin usar estructuras intermedias
    def __iter__(self):
        actual = self.head
        while actual is not None:
            yield actual.cancion
            actual = actual.siguiente

    # Complejidad: O(n)
    # Generador que recorre los nodos y retorna las canciones de la lista
    def listar(self):
        return self.__iter__()

    # Complejidad: O(n)
    def buscar_por_id(self,id_buscado):
        actual = self.head

        while(actual is not None):
            if actual.cancion.id == id_buscado:
                return actual.cancion
            actual = actual.siguiente
        return actual
    
    # Complejidad: O(n)
    # Generador que produce las canciones que coinciden con el criterio de busqueda
    def buscar_por_nombre(self,busqueda,criterio):
        actual = self.head

        while actual is not None:
            if criterio == 1 or criterio == "titulo":
                if busqueda.casefold() in actual.cancion.titulo.casefold():
                    yield actual.cancion
            elif criterio == 2 or criterio == "artista":
                if busqueda.casefold() in actual.cancion.artista.casefold():
                    yield actual.cancion
            actual = actual.siguiente

    # Complejidad: O(n)
    def eliminar_por_id(self,id_buscado):
        actual = self.head

        if(self.head is None):
            return False

        if(self.head.cancion.id == id_buscado):
            self.head = self.head.siguiente
            return True

        while(actual.siguiente is not None):
            if(actual.siguiente.cancion.id == id_buscado):
                actual.siguiente = actual.siguiente.siguiente
                return True
            actual = actual.siguiente
            
        return False