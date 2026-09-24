from src.services.CatalogoService import CatalogoService
from src.services.PlaylistService import PlaylistService
from src.ui.consolehelpers import (
    limpiar_pantalla,
    dibujar_menu,
    dibujar_inputs,
    capturar_opcion,
)


class Interfaz:
    def __init__(
        self, catalogo_service: CatalogoService, playlist_service: PlaylistService
    ):
        self.catalogo_service = catalogo_service
        self.playlist_service = playlist_service

    def pausar(self):
        input("\nPresione Enter para continuar...")

    def iniciar(self):
        opciones_principales = (
            "1. Gestion de Catalogo",
            "2. Gestion de Playlist y Reproductor",
            "3. Salir",
        )

        while True:
            limpiar_pantalla()
            dibujar_menu(opciones_principales, "REPRODUCTOR DE MUSICA")
            opcion = capturar_opcion(1, 3)

            if opcion == 1:
                self.menu_catalogo()
            elif opcion == 2:
                self.menu_playlist()
            elif opcion == 3:
                limpiar_pantalla()
                self.playlist_service.cerrarReproductor()
                print("Cerrando aplicacion... Hasta luego!")
                break

    def menu_catalogo(self):
        opciones = (
            "1. Agregar nuevas canciones al catalogo",
            "2. Listar todas las canciones registradas",
            "3. Buscar canciones por titulo o artista",
            "4. Editar una cancion",
            "5. Consultar los detalles de una cancion por su ID",
            "6. Eliminar una cancion del catalogo",
            "7. Regresar al menu principal",
        )

        while True:
            limpiar_pantalla()
            dibujar_menu(opciones, "GESTION DE CATALOGO")
            opcion = capturar_opcion(1, 7)

            if opcion == 1:
                limpiar_pantalla()
                dibujar_inputs("REGISTRAR CANCION")
                titulo = input("Titulo: ").strip()
                artista = input("Artista: ").strip()
                duracion = input("Duracion (en segundos): ").strip()
                archivo = input(
                    "Nombre de archivo en media/ (ej. cancion.mp3): "
                ).strip()

                exito, mensaje = self.catalogo_service.agregarCancion(
                    titulo, artista, duracion, archivo
                )
                print(f"\n{mensaje}")
                self.pausar()

            elif opcion == 2:
                limpiar_pantalla()
                dibujar_inputs("CATALOGO DE CANCIONES")
                exito, mensaje = self.catalogo_service.listarCanciones()
                if not exito:
                    print(f"\n{mensaje}")
                self.pausar()

            elif opcion == 3:
                limpiar_pantalla()
                dibujar_inputs("BUSCAR POR TEXTO")
                print("1. Buscar por Titulo")
                print("2. Buscar por Artista")
                criterio_opc = capturar_opcion(1, 2, "Seleccione criterio: ")
                criterio = "titulo" if criterio_opc == 1 else "artista"

                termino = input("Ingrese el termino de busqueda: ").strip()
                exito, mensaje = self.catalogo_service.buscarCancion(termino, criterio)
                if not exito:
                    print(f"\n{mensaje}")
                self.pausar()

            elif opcion == 4:
                limpiar_pantalla()
                dibujar_inputs("EDITAR CANCION")
                self.catalogo_service.listarCanciones()
                id_editar = capturar_opcion(
                    1, 999999, "Ingrese el ID de la cancion a editar: "
                )
                cancion = self.catalogo_service.catalogo.buscar_por_id(id_editar)
                if cancion is None:
                    print("\nNo existe ninguna cancion con este ID.")
                else:
                    print(f"\nDatos actuales:\n{cancion}")
                    print("\n(Presione Enter sin escribir nada para conservar el dato actual)")
                    nuevo_titulo = input(f"Nuevo titulo [{cancion.titulo}]: ").strip() or None
                    nuevo_artista = input(f"Nuevo artista [{cancion.artista}]: ").strip() or None
                    nueva_duracion = input(f"Nueva duracion en segundos [{cancion.duracion}]: ").strip() or None
                    nuevo_archivo = input(f"Nuevo archivo [{cancion.archivo}]: ").strip() or None

                    exito, mensaje = self.catalogo_service.editarCancion(
                        id_editar, nuevo_titulo, nuevo_artista, nueva_duracion, nuevo_archivo
                    )
                    print(f"\n{mensaje}")
                self.pausar()

            elif opcion == 5:
                limpiar_pantalla()
                dibujar_inputs("CONSULTAR DETALLES POR ID")
                id_buscado = capturar_opcion(1, 999999, "Ingrese el ID: ")
                exito, resultado = self.catalogo_service.buscarPorId(id_buscado)
                if exito:
                    cancion, en_playlist = resultado
                    print("\nCancion encontrada:")
                    print(cancion)
                    print(f"Agregada a la playlist: {'Si' if en_playlist else 'No'}")
                else:
                    print(f"\n{resultado}")
                self.pausar()

            elif opcion == 6:
                limpiar_pantalla()
                dibujar_inputs("ELIMINAR CANCION DEL CATALOGO")
                exito_l, msg_l = self.catalogo_service.listarCanciones()
                if not exito_l:
                    print(f"\n{msg_l}")
                    self.pausar()
                else:
                    id_eliminar = capturar_opcion(
                        1, 999999, "Ingrese el ID a eliminar: "
                    )
                    cancion = self.catalogo_service.catalogo.buscar_por_id(id_eliminar)
                    if cancion is None:
                        print("\nError al eliminar: Cancion no encontrada")
                    else:
                        print(f"\nCancion seleccionada:\n{cancion}\n")
                        confirmacion = input("Esta seguro de que desea eliminar esta cancion? (s/n): ").strip().lower()
                        if confirmacion in ("s", "si"):
                            exito, mensaje = self.catalogo_service.eliminarPorId(id_eliminar)
                            print(f"\n{mensaje}")
                        else:
                            print("\nOperacion cancelada. No se elimino la cancion.")
                    self.pausar()

            elif opcion == 7:
                break

    def menu_playlist(self):
        opciones = (
            "1. Agregar canciones a la playlist a partir del catalogo",
            "2. Reproducir la cancion actual",
            "3. Avanzar a la siguiente cancion",
            "4. Retroceder a la cancion anterior",
            "5. Mostrar la playlist en orden directo e inverso",
            "6. Eliminar canciones especificas de la playlist",
            "7. Pausar / Reanudar",
            "8. Regresar al menu principal",
        )

        while True:
            limpiar_pantalla()
            dibujar_menu(opciones, "PLAYLIST Y REPRODUCTOR")
            opcion = capturar_opcion(1, 8)

            if opcion == 1:
                limpiar_pantalla()
                dibujar_inputs("AGREGAR A PLAYLIST")
                print("Canciones disponibles en el catalogo:\n")
                exito_disp, msg_disp = self.playlist_service.listarDisponibles()
                if not exito_disp:
                    print(f"\n{msg_disp}")
                    self.pausar()
                else:
                    print()
                    id_cancion = capturar_opcion(
                        1, 999999, "Ingrese el ID de la cancion: "
                    )
                    exito, mensaje = self.playlist_service.agregarCanciones(id_cancion)
                    print(f"\n{mensaje}")
                    self.pausar()

            elif opcion == 2:
                limpiar_pantalla()
                dibujar_inputs("REPRODUCIENDO")
                exito, resultado = self.playlist_service.reproducirActual()
                if exito:
                    print(f"\nReproduciendo: {resultado.titulo} - {resultado.artista}")
                else:
                    print(f"\n{resultado}")
                self.pausar()

            elif opcion == 3:
                limpiar_pantalla()
                dibujar_inputs("SIGUIENTE CANCION")
                exito, mensaje = self.playlist_service.siguienteCancion()
                print(f"\n{mensaje}")
                self.pausar()

            elif opcion == 4:
                limpiar_pantalla()
                dibujar_inputs("CANCION ANTERIOR")
                exito, mensaje = self.playlist_service.anteriorCancion()
                print(f"\n{mensaje}")
                self.pausar()

            elif opcion == 5:
                limpiar_pantalla()
                dibujar_inputs("MOSTRAR PLAYLIST")
                print("1. Orden normal (Head -> Tail)")
                print("2. Orden inverso (Tail -> Head)")
                modo = capturar_opcion(1, 2, "Seleccione el orden: ")

                if modo == 1:
                    exito, mensaje = self.playlist_service.listarPlaylist()
                else:
                    exito, mensaje = self.playlist_service.listarInverso()
                if not exito:
                    print(f"\n{mensaje}")
                self.pausar()

            elif opcion == 6:
                limpiar_pantalla()
                dibujar_inputs("ELIMINAR DE PLAYLIST")
                self.playlist_service.listarPlaylist()
                id_eliminar = capturar_opcion(
                    1, 999999, "Ingrese el ID de la cancion a eliminar: "
                )
                exito, mensaje = self.playlist_service.eliminarCanciones(id_eliminar)
                print(f"\n{mensaje}")
                self.pausar()

            elif opcion == 7:
                limpiar_pantalla()
                dibujar_inputs("CONTROL DE AUDIO")
                exito, mensaje = self.playlist_service.pausarOreanudar()
                print(f"\n{mensaje}")
                self.pausar()

            elif opcion == 8:
                break