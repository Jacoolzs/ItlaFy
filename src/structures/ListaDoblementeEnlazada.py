from NodoDoble import NodoDoble

class ListaDoblementeEnlazada:

    # Complejidad O(1)
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    # Complejidad O(1)
    def agregar(self,cancion):
        nuevaCancion = NodoDoble(cancion)
        
        if(self.head is None):
            self.head = nuevaCancion
            self.tail = nuevaCancion
            self.current = nuevaCancion
            return

        nuevaCancion.anterior = self.tail
        self.tail.siguiente = nuevaCancion
        self.tail = nuevaCancion

    # Complejidad O(1)
    def avanzar(self):
        if self.head is None:
            print("No hay canciones en la playlist")
            return
        
        if self.current.siguiente is None:
            self.current = self.head
            return
        else:
            self.current = self.current.siguiente
            return

    # Complejidad O(1)
    def retroceder(self):
        if self.head is None:
            print("No hay canciones en la playlist")
            return
        
        if self.current.anterior is None:
            self.current = self.tail
            return
        else:
            self.current = self.current.anterior
            return

    # Complejidad O(n)
    def mostrar_playlist(self,inverso):
    
        if self.head is None:
            print("No hay canciones en la playlist")
            return
        
        if inverso:
            actual = self.tail
            while actual is not None:
                print(actual.cancion)
                actual = actual.anterior
            return
        else:
            actual = self.head
            while actual is not None:
                print(actual.cancion)
                actual = actual.siguiente
            return

    # Complejidad O(n)
    def eliminar_por_id(self,id_eliminar):
        if self.head is None:
            print("No hay canciones en la playlist")
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

                print("Cancion eliminada con exito")
                return True

            actual = actual.siguiente
        print("No se han encontrado resultados")
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