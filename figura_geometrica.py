# ARCHIVO 1: figura_geometrica.py

class FiguraGeometrica:

    def __init__(self, ancho, alto):
        self._ancho = None
        self._alto = None
        self.ancho = ancho
        self.alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        if valor <= 0:
            raise ValueError("El ancho debe ser mayor que 0")
        self._ancho = valor

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        if valor <= 0:
            raise ValueError("El alto debe ser mayor que 0")
        self._alto = valor

    def area(self):
        return self._ancho * self._alto

    def perimetro(self):

        pass

    def __str__(self):
        """Representación en cadena de la figura."""
        return f"FiguraGeometrica [Ancho: {self._ancho}, Alto: {self._alto}]"