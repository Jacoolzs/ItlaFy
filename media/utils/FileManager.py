import os

class FileManager:
    # Complejidad: O(1)
    def __init__(self):
        pass

    # Complejidad: O(1)
    def validar_archivo(self,nombreArchivo):
        if nombreArchivo.lower().endswith(('.mp3','.wav')):
            ruta = os.path.join("media", nombreArchivo)
            if os.path.exists(ruta):
                return True
        return False

    # Complejidad: O(1)
    def eliminar_archivo(self,nombreArchivo):
        if self.validar_archivo(nombreArchivo):
            os.remove(os.path.join('media',nombreArchivo))
            return True
        return False