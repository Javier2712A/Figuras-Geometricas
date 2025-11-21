# ARCHIVO 3: rectangulo.py


from figura_geometrica import FiguraGeometrica


class Rectangulo(FiguraGeometrica):
    """Clase que representa un rectángulo."""

    def __init__(self, ancho, alto):

        super().__init__(ancho, alto)

    def area(self):

        return self._ancho * self._alto

    def perimetro(self):

        return 2 * (self._ancho + self._alto)

    def __str__(self):
        """Representación en cadena del rectángulo."""
        return f"Rectangulo [Ancho: {self._ancho}, Alto: {self._alto}]"
