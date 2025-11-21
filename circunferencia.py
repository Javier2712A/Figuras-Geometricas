# ARCHIVO 4: circunferencia.py

import math
from figura_geometrica import FiguraGeometrica


class Circunferencia(FiguraGeometrica):

    def __init__(self, radio):

        # Usamos el radio como ancho y alto para aprovechar la validación
        super().__init__(radio, radio)

    @property
    def radio(self):
        """Obtiene el radio de la circunferencia."""
        return self._ancho

    @radio.setter
    def radio(self, valor):
        """Establece el radio de la circunferencia."""
        self.ancho = valor
        self.alto = valor

    def area(self):

        return math.pi * (self._ancho ** 2)

    def perimetro(self):

        return 2 * math.pi * self._ancho

    def __str__(self):
        """Representación en cadena de la circunferencia."""
        return f"Circunferencia [Radio: {self._ancho}]"