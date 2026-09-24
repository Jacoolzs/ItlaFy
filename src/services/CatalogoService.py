from src.utils.FileManager import FileManager
from src.structures.ListaSimple import ListaSimple
from src.structures.ListaDoblementeEnlazada import ListaDoblementeEnlazada
from src.models.Cancion import Cancion

class CatalogoService:
    # complejidad O(1)
    def __init__(self,listaCatalogo: ListaSimple, listaPlaylist: ListaDoblementeEnlazada, fileManager: FileManager):
        self.catalogo = listaCatalogo
        self.playlist = listaPlaylist
        self.fileManager = fileManager
        pass

    # complejidad O(n)
    def agregarCancion(self, titulo, artista,duracion,nombreArchivo):
        if len(titulo.strip()) == 0:
            return False, "Debe introducir un titulo para la cancion."
        
        if len(artista.strip()) == 0:
            return False, "Debe introducir un artista para la cancion"
        
        try:
            duracion_num = float(duracion)
            if duracion_num <= 0:
                return False, "Debe introducir una duracion valida para la cancion"
        except (ValueError, TypeError):
            return False, "Debe introducir una duracion valida para la cancion"
        
        if len(nombreArchivo.strip()) == 0:
            return False, "Debe introducir un nombre para el archivo"

        if self.fileManager.validar_archivo(nombreArchivo):
            nuevaCancion = Cancion(titulo,artista,duracion_num,nombreArchivo)
            self.catalogo.agregar(nuevaCancion)
            return True, "Cancion agregada exitosamente."
        else:
            return False, "El nombre del archivo no se ha encontrado"

    # complejidad O(n)
    # muestra las canciones registradas en el catalogo
    def listarCancion(self):
        if self.catalogo.head is None:
            return False, "No hay canciones registradas"
        for cancion in self.catalogo:
            print(cancion)
            print("-" * 25)
        return True, None

    # complejidad O(n)
    # busca canciones por titulo o artista
    def buscarCancion(self,cancion,criterio):
        encontrados = False
        for c in self.catalogo.buscar_por_nombre(cancion,criterio):
            print(c)
            print("-" * 25)
            encontrados = True
        if not encontrados:
            return False, "No se encontraron coincidencias"
        return True, None

    # complejidad O(n)
    # edita los datos de la cancion validando los campos
    def editarCancion(self,idCancion,titulo,artista,duracion,nombreArchivo):
        cancion:Cancion = self.catalogo.buscar_por_id(idCancion)

        if cancion is None:
            return False,"No existe ninguna cancion con este ID"

        nuevo_titulo = cancion.titulo
        if titulo is not None and titulo != cancion.titulo:
            if len(titulo.strip()) == 0:
                return False, "Debe introducir un titulo para la cancion."
            nuevo_titulo = titulo

        nuevo_artista = cancion.artista
        if artista is not None and artista != cancion.artista:
            if len(artista.strip()) == 0:
                return False, "Debe introducir un artista para la cancion"
            nuevo_artista = artista

        nueva_duracion = cancion.duracion
        if duracion is not None and duracion != cancion.duracion:
            try:
                duracion_num = float(duracion)
                if duracion_num <= 0:
                    return False, "Debe introducir una duracion valida para la cancion"
                nueva_duracion = duracion_num
            except (ValueError, TypeError):
                return False, "Debe introducir una duracion valida para la cancion"

        nuevo_archivo = cancion.archivo
        if nombreArchivo is not None and nombreArchivo != cancion.archivo:
            if len(nombreArchivo.strip()) == 0:
                return False, "Debe introducir un nombre para el archivo"

            if self.fileManager.validar_archivo(nombreArchivo):
                nuevo_archivo = nombreArchivo
            else:
                return False, "El nombre del archivo no existe en media/ o su extension no es valida (.mp3, .wav)"

        # aplica los cambios
        cancion.titulo = nuevo_titulo
        cancion.artista = nuevo_artista
        cancion.duracion = nueva_duracion
        cancion.archivo = nuevo_archivo

        return True, "Cancion editada con exito"
    
    # complejidad O(n)
    def buscarPorId(self, idCancion):
        cancion = self.catalogo.buscar_por_id(idCancion)
        if cancion is None:
            return False, "Cancion no encontrada"
        else:
            existeEnPlaylist = self.playlist.verificar_si_existe(cancion.id)
            return True, (cancion,existeEnPlaylist)

    # complejidad O(n)
    def eliminarPorId(self, idCancion):
        cancion:Cancion = self.catalogo.buscar_por_id(idCancion)
        if cancion is None:
            return False, "Error al eliminar: Cancion no encontrada"
        else:
            existeEnPlaylist = self.playlist.verificar_si_existe(cancion.id)
            if(existeEnPlaylist):
                return False, "Error al eliminar: La cancion se encuentra en una playlist"
            else:
                if self.catalogo.eliminar_por_id(idCancion):
                    self.fileManager.eliminar_archivo(cancion.archivo)
                    return True,"Cancion eliminada con exito."
                return False, "Error al eliminar la cancion de la lista"

    # alias para la interfaz
    listarCanciones = listarCancion
    buscarCancionPorId = buscarPorId
    eliminarCancion = eliminarPorId