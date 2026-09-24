class NodoDoble:

# complejidad O(1)
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None
        self.anterior = None