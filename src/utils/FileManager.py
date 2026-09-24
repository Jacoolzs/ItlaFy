import os

class FileManager:
    def __init__(self):
        self.base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        self.media_dir = os.path.join(self.base_dir, "media")
        if not os.path.exists(self.media_dir):
            os.makedirs(self.media_dir, exist_ok=True)

    def validar_archivo(self, nombreArchivo):
        if nombreArchivo.lower().endswith(('.mp3', '.wav')):
            ruta = self.construir_ruta(nombreArchivo)
            if os.path.exists(ruta):
                return True
        return False

    def eliminar_archivo(self, nombreArchivo):
        if self.validar_archivo(nombreArchivo):
            os.remove(self.construir_ruta(nombreArchivo))
            return True
        return False

    def validar_ruta(self, ruta):
        return os.path.exists(ruta)

    def construir_ruta(self, nombreArchivo):
        return os.path.join(self.media_dir, nombreArchivo)
