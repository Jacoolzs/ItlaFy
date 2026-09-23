from media.utils.FileManager import FileManager
from structures.ListaSimple import ListaSimple
from structures.ListaDoblementeEnlazada import ListaDoblementeEnlazada
from src.models.Cancion import Cancion

class CatalogoService:
    # Complejidad O(1)
    def __init__(self,listaCatalogo: ListaSimple, listaPlaylist: ListaDoblementeEnlazada, fileManager: FileManager):
        self.catalogo = listaCatalogo
        self.playlist = listaPlaylist
        self.fileManager = fileManager
        pass

    # Complejidad O(n)
    def agregarCancion(self, titulo, artista,duracion,nombreArchivo):
        if len(titulo.strip()) == 0:
            return False, "Debe introducir un titulo para la cancion."
        
        if len(artista.strip()) == 0:
            return False, "Debe introducir un artista para la cancion"
        
        if duracion <= 0:
            return False, "Debe introducir una duracion valida para la cancion"
        
        if len(nombreArchivo.strip()) == 0:
            return False, "Debe introducir un nombre para el archivo"

        if self.fileManager.validar_archivo(nombreArchivo):
            nuevaCancion = Cancion(titulo,artista,duracion,nombreArchivo)
            self.catalogo.agregar(nuevaCancion)
            return True, "Cancion agregada exitosamente."
        else:
            return False, "El nombre del archivo no se ha encontrado"

    # Complejidad O(n)
    def listarCancion(self):
        if(self.catalogo.head is None):
            return False, "No hay canciones registradas"
        else:
            self.catalogo.listar()
            return True, None

    def buscarCancion(self,cancion,criterio):
        resultados = self.catalogo.buscar_por_nombre(cancion,criterio)
        if not resultados:
            return resultados, "No se encontraron coincidencias"
        return resultados, None

    # Complejidad O(n)

    def editarCancion(self,idCancion,titulo,artista,duracion,nombreArchivo):
        cancion:Cancion = self.catalogo.buscar_por_id(idCancion)

        if cancion is None:
            return False,"No existe ninguna cancion con este ID"

        if titulo is not None and titulo!=cancion.titulo :
            if len(titulo.strip()) == 0:
                return False, "Debe introducir un titulo para la cancion."
            cancion.titulo = titulo
        if artista is not None and artista!=cancion.artista:       
            if len(artista.strip()) == 0:
                return False, "Debe introducir un artista para la cancion"
            cancion.artista = artista

        if duracion is not None and duracion!=cancion.duracion:
            if float(duracion) <= 0:
                return False, "Debe introducir una duracion valida para la cancion"
            cancion.duracion = duracion

        if nombreArchivo is not None and nombreArchivo!=cancion.archivo:
            if len(nombreArchivo.strip()) == 0:
                return False, "Debe introducir un nombre para el archivo"

            if self.fileManager.validar_archivo(nombreArchivo):
                cancion.archivo = nombreArchivo
            else:
                return False,"El nombre del archivo no existe"
        return True, "Cancion editada con exito"
    
    # Complejidad O(n)
    def buscarPorId(self, idCancion):
        cancion = self.catalogo.buscar_por_id(idCancion)
        if cancion is None:
            return False, "Cancion no encontrada"
        else:
            existeEnPlaylist = self.playlist.verificar_si_existe(cancion)
            return True, (cancion,existeEnPlaylist)

    # Complejidad O(n)
    def eliminarPorId(self, idCancion):
        cancion:Cancion = self.catalogo.buscar_por_id(idCancion)
        if cancion is None:
            return False, "Error al eliminar: Cancion no encontrada"
        else:
            existeEnPlaylist = self.playlist.verificar_si_existe(cancion)
            if(existeEnPlaylist):
                return False, "Error al eliminar: La cancion se encuentra en una playlist"
            else:
                if self.catalogo.eliminar_por_id(idCancion):
                    self.fileManager.eliminar_archivo(cancion.archivo)
                    return True,"Cancion eliminada con exito."
                return False, "Error al eliminar la cancion de la lista"