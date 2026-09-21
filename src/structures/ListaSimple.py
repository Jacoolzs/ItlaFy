from NodoSimple import NodoSimple
class ListaSimple:

    # Complejidad: O(1)
    def __init__(self):
        self.head = None

    # Complejidad: O(n)
    def agregar(self, cancion):

        nuevaCancion = NodoSimple(cancion)

        if self.head is None:
            self.head = nuevaCancion
            return

        actual = self.head
        while(actual.siguiente is not None):
            actual = actual.siguiente

        actual.siguiente = nuevaCancion

    # Complejidad: O(n)
    def listar(self):
        actual = self.head

        if(actual is None):
            print("No hay canciones registradas")
            return

        while(actual is not None):
            print(actual.cancion)
            actual = actual.siguiente

    # Complejidad: O(n)
    def buscar_por_id(self,id_buscado):
        actual = self.head

        while(actual is not None):
            if actual.cancion.id == id_buscado:
                return actual.cancion
            actual = actual.siguiente
        print("No se encontraron coincidencias")
        return None
    
    # Complejidad: O(n)
    def buscar_por_nombre(self,busqueda,criterio):
        actual = self.head
        encontrados = False

        while(actual is not None):
            if(criterio == 1):
                if(busqueda.casefold() in actual.cancion.titulo.casefold()):
                    print(actual.cancion)
                    encontrados = True
            elif(criterio == 2):
                if(busqueda.casefold() in actual.cancion.artista.casefold()):
                    print(actual.cancion)
                    encontrados = True
            actual = actual.siguiente

        if not encontrados: print("No se encontraron coincidencias")

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