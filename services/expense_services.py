from models.expense import Gasto
from data.repository import RepositorioGastos

class ServicioGastos:
    """
    Contiene la lógica de negocio relacionada con los gastos.
    Actúa como intermediario entre la interfaz y la persistencia.
    """
    def __init__(self, repositorio = None):
        self.repositorio = repositorio or RepositorioGastos()

    def agregar_gasto (self, importe, categoria, fecha, descripcion = ""):
        """
        Crea un gasto válido y lo guarda.
        """
        gasto = Gasto(
            importe=importe,
            categoria=categoria,
            fecha=fecha,
            descripcion=descripcion,
        )
        self.repositorio.guardar_gasto(gasto)
        return gasto
    
    def obtener_gastos(self):
        """
        Devuelve todos los gastos almacenados como objetos Gasto.
        """
        datos = self.repositorio.obtener_gastos()
        return [self._dict_a_gasto(dato) for dato in datos]
    
    def obtener_resumen(self):
        """
        Devuelve un resumen total de gastos por categoría.
        """
        resumen = {}
        for gasto in self.obtener_gastos():
            resumen[gasto.categoria] = resumen.get(gasto.categoria, 0) + gasto.importe
        return resumen

    def _dict_a_gasto(self, datos):
        """
        Convierte un diccionario en un objeto Gasto.
        """
        return Gasto(
            importe=datos["importe"],
            categoria=datos["categoria"],
            fecha=datos["fecha"],
            descripcion=datos.get("descripcion", ""),
        )
    
    def resetear_gastos(self):
        """
        Borra todos los gastos almacenados.
        """
        self.repositorio.borrar_gastos()
