from src.structures.ListaDoblementeEnlazada import ListaDoblementeEnlazada
from src.structures.ListaSimple import ListaSimple
from src.models.Cancion import Cancion
from src.utils.FileManager import FileManager
import pygame

class PlaylistService:

    # complejidad O(1)
    def __init__(self,listaCatalogo:ListaSimple,listaPlaylist:ListaDoblementeEnlazada,fileManager:FileManager):
        self.listaCatalogo = listaCatalogo
        self.listaPlaylist = listaPlaylist
        self.pausado = False
        self.fileManager = fileManager
        pygame.mixer.init()

    
    # complejidad O(n)
    # canciones disponibles que no estan en la playlist
    def listarDisponibles(self):
        actual = self.listaCatalogo.head
        if actual is None:
            return False, "No hay canciones registradas en el catalogo."

        hay_disponibles = False
        while actual is not None:
            if not self.listaPlaylist.verificar_si_existe(actual.cancion.id):
                print(actual.cancion)
                hay_disponibles = True
            actual = actual.siguiente

        if not hay_disponibles:
            return False, "Todas las canciones del catalogo ya han sido agregadas a la playlist."
        return True, None

    # complejidad O(n)
    # agrega la cancion al final de la playlist
    def agregarCanciones(self,idCancion):
        cancion: Cancion = self.listaCatalogo.buscar_por_id(idCancion)

        if cancion is None:
            return False, "La cancion seleccionada no existe"
        
        if self.listaPlaylist.verificar_si_existe(cancion.id):
            return False, "La cancion ya se encuentra en la playlist"
        
        if self.listaPlaylist.agregar(cancion):
            return True,"Cancion agregada con exito a la playlist"
        
        else:
            return False,"Hubo un error al agregar la cancion a la playlist"
        
    # complejidad O(n)
    # elimina cancion y actualiza la actual si aplica
    def eliminarCanciones(self, idCancion):
        if self.listaPlaylist.head is None:
            return False, "La playlist esta vacia"

        cancionActual: Cancion = self.listaPlaylist.actual()
        era_actual = (cancionActual is not None and cancionActual.id == idCancion)

        if era_actual:
            pygame.mixer.music.stop()

        if self.listaPlaylist.eliminar_por_id(idCancion):
            if era_actual:
                nueva_actual = self.listaPlaylist.actual()
                if nueva_actual:
                    return True, f"Cancion eliminada con exito. Nueva cancion actual: {nueva_actual.titulo} - {nueva_actual.artista}"
                else:
                    return True, "Cancion eliminada con exito. La playlist ha quedado vacia."
            return True, "Cancion eliminada con exito"
        else:
            return False, "La cancion no se encontraba en la playlist"

    # complejidad O(n)
    # muestra la playlist en orden directo o inverso
    def mostrarPlaylist(self, inverso=False):
        if self.listaPlaylist.head is None:
            return False, "La playlist esta vacia"
        for cancion in self.listaPlaylist.recorrer(inverso):
            print(f"{cancion.id} - {cancion.titulo} - {cancion.artista}")
        return True, None
        
    # complejidad O(1)
    # reproduce la cancion actual o la primera si no hay seleccion
    def reproducirActual(self):
        if self.listaPlaylist.head is None:
            return False, "No hay canciones en la playlist para reproducir"

        # si no hay actual toma la primera
        if self.listaPlaylist.current is None:
            self.listaPlaylist.current = self.listaPlaylist.head

        cancionActual: Cancion = self.listaPlaylist.actual()
        if cancionActual is None:
            return False, "No hay canciones en la playlist para reproducir"
        
        ruta = self.fileManager.construir_ruta(cancionActual.archivo)
        if not self.fileManager.validar_ruta(ruta):
            return False, f"El archivo de audio '{cancionActual.archivo}' no se ha encontrado en media/"
        
        try:
            pygame.mixer.music.load(ruta)
            pygame.mixer.music.play()
            self.pausado = False
            return True, cancionActual
        except Exception as e:
            return False, f"Error al reproducir audio: {str(e)}"

    # complejidad O(1)
    # pausa o reanuda la musica
    def pausarOreanudar(self):
        cancionActual:Cancion = self.listaPlaylist.actual()
        
        if cancionActual is None:
            return False,"No hay canciones en la playlist"

        if self.pausado is True:
            pygame.mixer.music.unpause()
            self.pausado = False
            return True, "Reproduccion reanudada"
        elif pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.pausado = True
            return True, "Reproduccion pausada"
        else:
            return False, "No hay canciones sonando actualmente"

    # complejidad O(1)
    # pasa a la siguiente cancion
    def siguienteCancion(self):
        if not self.listaPlaylist.avanzar():
            return False,"No hay canciones en la playlist"
        else:
            cancion = self.listaPlaylist.actual()
            return True, f"Cancion actual: {cancion.titulo} - {cancion.artista}"

    # complejidad O(1)
    # vuelve a la cancion anterior
    def anteriorCancion(self):
        if not self.listaPlaylist.retroceder():
            return False,"No hay canciones en la playlist"
        else:
            cancion = self.listaPlaylist.actual()
            return True, f"Cancion actual: {cancion.titulo} - {cancion.artista}"

    # alias y metodos para la interfaz
    def listarPlaylist(self):
        return self.mostrarPlaylist(inverso=False)

    def listarInverso(self):
        return self.mostrarPlaylist(inverso=True)

    agregarCancion = agregarCanciones
    eliminarCancion = eliminarCanciones
    alternarPausa = pausarOreanudar

    # complejidad O(1)
    # detiene y cierra el audio de pygame
    def cerrarReproductor(self):
        try:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
        except Exception:
            pass