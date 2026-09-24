import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.structures.ListaSimple import ListaSimple
from src.structures.ListaDoblementeEnlazada import ListaDoblementeEnlazada
from src.services.CatalogoService import CatalogoService
from src.services.PlaylistService import PlaylistService
from src.utils.FileManager import FileManager
from src.ui.interfaz import Interfaz


def main():
    catalogo_lista = ListaSimple()
    playlist_lista = ListaDoblementeEnlazada()
    file_manager = FileManager()

    catalogo_service = CatalogoService(catalogo_lista, playlist_lista, file_manager)
    playlist_service = PlaylistService(catalogo_lista, playlist_lista, file_manager)

    app = Interfaz(catalogo_service, playlist_service)
    app.iniciar()


if __name__ == "__main__":
    main()