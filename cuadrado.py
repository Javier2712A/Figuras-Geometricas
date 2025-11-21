# ARCHIVO 2: cuadrado.py

from figura_geometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica):

    def __init__(self, lado):

        super().__init__(lado, lado)

    def area(self):

        return self._ancho ** 2

    def perimetro(self):

        return 4 * self._ancho

    def __str__(self):
        """Representación en cadena del cuadrado."""
        return f"Cuadrado [Lado: {self._ancho}]"