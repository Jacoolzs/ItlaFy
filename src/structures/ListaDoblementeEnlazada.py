from src.structures.NodoDoble import NodoDoble

class ListaDoblementeEnlazada:

    # Complejidad O(1)
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    # Complejidad O(1)
    # Retorna el objeto cancion almacenado en el nodo actual
    def actual(self):
        if self.current is None:
            return None
        return self.current.cancion

    # Complejidad O(1)
    def agregar(self,cancion):
        nuevaCancion = NodoDoble(cancion)
        
        if(self.head is None):
            self.head = nuevaCancion
            self.tail = nuevaCancion
            self.current = nuevaCancion
            return True

        nuevaCancion.anterior = self.tail
        self.tail.siguiente = nuevaCancion
        self.tail = nuevaCancion
        return True

    # Complejidad O(1)
    def avanzar(self):
        if self.head is None:
            return False
        
        if self.current.siguiente is None:
            self.current = self.head
            return True
        else:
            self.current = self.current.siguiente
            return True

    # Complejidad O(1)
    def retroceder(self):
        if self.head is None:
            return False
        
        if self.current.anterior is None:
            self.current = self.tail
            return True
        else:
            self.current = self.current.anterior
            return True

    # Complejidad O(n)
    # Permite iterar hacia adelante por defecto sobre la lista doblemente enlazada
    def __iter__(self):
        return self.recorrer(inverso=False)

    # Complejidad O(n)
    # Generador que recorre la playlist en sentido directo o inverso sin usar estructuras externas
    def recorrer(self, inverso=False):
        actual = self.tail if inverso else self.head
        while actual is not None:
            yield actual.cancion
            actual = actual.anterior if inverso else actual.siguiente

    # Complejidad O(n)
    # Generador compatible para obtener las canciones de la lista
    def mostrar_playlist(self, inverso):
        return self.recorrer(inverso)

    # Complejidad O(n)
    def eliminar_por_id(self,id_eliminar):
        if self.head is None:
            return False

        actual = self.head
        while actual is not None:
            if actual.cancion.id == id_eliminar:

                # Si la cancion a eliminar es el current
                if actual == self.current:

                    # Valido que tenga siguiente y anterior
                    if actual.siguiente is not None:
                        self.current = actual.siguiente

                    elif actual.anterior is not None:
                        self.current = actual.anterior

                    else:
                        self.current = None
                
                if actual == self.head and actual == self.tail:
                    self.head = None
                    self.tail = None
                
                elif actual == self.head:
                    self.head = actual.siguiente
                    self.head.anterior = None

                elif actual == self.tail:
                    self.tail = actual.anterior
                    self.tail.siguiente = None

                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                return True

            actual = actual.siguiente
        return False

    # Complejidad O(n)

    def verificar_si_existe(self,id_buscado):
        actual = self.head

        while actual is not None:
            if actual.cancion.id == id_buscado:
                return True
            else:
                actual = actual.siguiente
                
        return False