from datetime import datetime


class Gasto:
    """
    Representa un gasto realizado por el usuario.
    Una instancia de Gasto siempre es válida desde el momento de su creación.
    """

    def __init__(self, importe, categoria, fecha, descripcion=""):
        self.importe = self._validar_importe(importe)
        self.categoria = self._validar_categoria(categoria)
        self.fecha = self._validar_fecha(fecha)
        self.descripcion = descripcion

    def _validar_importe(self, importe):
        if not isinstance(importe, (int, float)):
            raise TypeError("El importe debe ser un número")

        if importe <= 0:
            raise ValueError("El importe debe ser mayor que cero")

        return float(importe)

    def _validar_categoria(self, categoria):
        if not isinstance(categoria, str):
            raise TypeError("La categoría debe ser un texto")

        if not categoria.strip():
            raise ValueError("La categoría no puede estar vacía")

        return categoria.strip()

    def _validar_fecha(self, fecha):
        # Si ya es un datetime, devolver solo la fecha
        if isinstance(fecha, datetime):
            return fecha.date()

        # Si es un string, intentar varios formatos
        if isinstance(fecha, str):
            # Formato DD-MM-YYYY (entrada de usuario)
            try:
                return datetime.strptime(fecha, "%d-%m-%Y").date()
            except ValueError:
                pass

            # Formato YYYY-MM-DD (datos guardados / JSON)
            try:
                return datetime.strptime(fecha, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError(
                    "La fecha debe tener el formato DD-MM-YYYY"
                )

        raise TypeError("La fecha debe ser un texto o un objeto datetime")

    def __str__(self):
        return (
            f"{self.fecha.strftime('%d-%m-%Y')} | "
            f"{self.categoria} | "
            f"{self.importe:.2f} € | "
            f"{self.descripcion}"
        )
