# complejidad: O(1)
class Cancion:
    _contador_id = 1
    def __init__(self,titulo,artista,duracion,archivo):
        self.id = Cancion._contador_id
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion
        self.archivo = archivo
        Cancion._contador_id += 1
        
# complejidad: O(1)
    def __str__(self):
        return f"ID:{self.id}\nTitulo: {self.titulo}\nArtista: {self.artista}\nDuracion: {self.duracion}\nNombre del archivo: {self.archivo}"