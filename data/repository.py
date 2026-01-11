import json
from pathlib import Path
from models.expense import Gasto


class RepositorioGastos:
    """
    Gestiona la persistencia de los gastos.
    Se encarga de guardar y recuperar gastos desde un archivo JSON.
    """

    def __init__(self, ruta_archivo="data/gastos.json"):
        self.ruta_archivo = Path(ruta_archivo)
        self._asegurar_archivo()

    def _asegurar_archivo(self):
        """
        Asegura que el archivo de datos existe.
        Si no existe, lo crea con una lista vacía.
        """
        if not self.ruta_archivo.exists():
            self.ruta_archivo.parent.mkdir(parents=True, exist_ok=True)
            self.ruta_archivo.write_text("[]", encoding="utf-8")

    def guardar_gasto(self, gasto):
        """
        Guarda un gasto en el archivo.
        """
        gastos = self.obtener_gastos()
        gastos.append(self._gasto_a_dict(gasto))

        with self.ruta_archivo.open("w", encoding="utf-8") as archivo:
            json.dump(gastos, archivo, ensure_ascii=False, indent=4)

    def obtener_gastos(self):
        """
        Devuelve una lista de gastos almacenados.
        """
        with self.ruta_archivo.open("r", encoding="utf-8") as archivo:
            return json.load(archivo)

    def _gasto_a_dict(self, gasto):
        """
        Convierte un objeto Gasto a un diccionario serializable.
        """
        return {
            "importe": gasto.importe,
            "categoria": gasto.categoria,
            "fecha": gasto.fecha.isoformat(),
            "descripcion": gasto.descripcion,
        }
    
    def borrar_gastos(self):
        """
        Elimina todos los gastos guardados.
        """
        with self.ruta_archivo.open("w", encoding="utf-8") as archivo:
           archivo.write("[]")
