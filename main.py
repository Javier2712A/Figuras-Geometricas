# ARCHIVO 5: main.py

from datetime import datetime
from cuadrado import Cuadrado
from rectangulo import Rectangulo
from circunferencia import Circunferencia


def sumar_areas(figuras):
    total = 0
    for figura in figuras:
        total += figura.area()
    return total


def sumar_perimetros(figuras):
    total = 0
    for figura in figuras:
        total += figura.perimetro()
    return total


def imprimir_separador():
    """Imprime un separador visual."""

def main():
    """Función principal que ejecuta el programa."""
    print("TALLER DE POO - FIGURAS GEOMÉTRICAS")
    print(f"Fecha y hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # ==================== CREACIÓN DE CUADRADOS ====================
    imprimir_separador()
    print("1. CREACIÓN DE CUADRADOS")

    cuadrado1 = Cuadrado(5)
    print(f"Cuadrado 1 creado: {cuadrado1}")
    print(f"Área: {cuadrado1.area()}")
    print(f"Perímetro: {cuadrado1.perimetro()}")

    cuadrado2 = Cuadrado(8)
    print(f"Cuadrado 2 creado: {cuadrado2}")
    print(f"Área: {cuadrado2.area()}")
    print(f"Perímetro: {cuadrado2.perimetro()}")

    # ==================== CREACIÓN DE RECTÁNGULOS ====================
    imprimir_separador()
    print("2. CREACIÓN DE RECTÁNGULOS")

    rectangulo1 = Rectangulo(4, 6)
    print(f"Rectángulo 1 creado: {rectangulo1}")
    print(f"Área: {rectangulo1.area()}")
    print(f"Perímetro: {rectangulo1.perimetro()}")

    rectangulo2 = Rectangulo(10, 3)
    print(f"Rectángulo 2 creado: {rectangulo2}")
    print(f"Área: {rectangulo2.area()}")
    print(f"Perímetro: {rectangulo2.perimetro()}")

    # ==================== CREACIÓN DE CIRCUNFERENCIAS ====================
    imprimir_separador()
    print("3. CREACIÓN DE CIRCUNFERENCIAS")

    circunferencia1 = Circunferencia(7)
    print(f"Circunferencia 1 creada: {circunferencia1}")
    print(f"  Área: {circunferencia1.area():.2f}")
    print(f"  Perímetro: {circunferencia1.perimetro():.2f}")

    # ==================== MODIFICACIÓN DE VALORES ====================
    imprimir_separador()
    print("4. MODIFICACIÓN DE VALORES (Encapsulamiento)")
    print(f"Cuadrado 1 antes: {cuadrado1}")
    cuadrado1.ancho = 10
    cuadrado1.alto = 10
    print(f"Cuadrado 1 después de modificar: {cuadrado1}")
    print(f"Nueva Área: {cuadrado1.area()}")
    print(f"Nuevo Perímetro: {cuadrado1.perimetro()}")

    print(f"Rectángulo 1 antes: {rectangulo1}")
    rectangulo1.ancho = 7
    rectangulo1.alto = 12
    print(f"Rectángulo 1 después de modificar: {rectangulo1}")
    print(f"Nueva Área: {rectangulo1.area()}")
    print(f"Nuevo Perímetro: {rectangulo1.perimetro()}")

    # ==================== VALIDACIÓN DE ERRORES ====================
    imprimir_separador()
    print("5. VALIDACIÓN DE ERRORES (Valores Inválidos)")

    print("Intentando crear un cuadrado con lado negativo...")
    try:
        cuadrado_invalido = Cuadrado(-5)
    except ValueError as e:
        print(f"  ✗ Error capturado: {e}")

    print("Intentando crear un rectángulo con ancho = 0...")
    try:
        rectangulo_invalido = Rectangulo(0, 5)
    except ValueError as e:
        print(f"  ✗ Error capturado: {e}")

    print("Intentando asignar alto negativo a un cuadrado existente...")
    try:
        cuadrado1.alto = -3
    except ValueError as e:
        print(f"  ✗ Error capturado: {e}")

    print("Intentando crear circunferencia con radio negativo...")
    try:
        circunferencia_invalida = Circunferencia(-2)
    except ValueError as e:
        print(f"  ✗ Error capturado: {e}")

    # ==================== POLIMORFISMO ====================
    imprimir_separador()
    print("6. DEMOSTRACIÓN DE POLIMORFISMO")

    # Lista con diferentes tipos de figuras
    figuras = [cuadrado1, cuadrado2, rectangulo1, rectangulo2, circunferencia1]

    print("Lista de figuras:")
    for i, figura in enumerate(figuras, 1):
        print(f"  {i}. {figura}")

    print("Cálculo usando polimorfismo:")
    print(f"  Suma total de áreas: {sumar_areas(figuras):.2f}")
    print(f"  Suma total de perímetros: {sumar_perimetros(figuras):.2f}")

    print("Detalle de áreas por figura:")
    for figura in figuras:
        print(f"  - {figura.__class__.__name__}: {figura.area():.2f}")

    print("Detalle de perímetros por figura:")
    for figura in figuras:
        print(f"  - {figura.__class__.__name__}: {figura.perimetro():.2f}")

    # ==================== RESUMEN FINAL ====================
    imprimir_separador()
    print("7. RESUMEN FINAL")
    print(" Encapsulamiento implementado con @property y @setter")
    print(" Validaciones funcionando correctamente")
    print(" Herencia implementada en todas las clases")
    print(" Polimorfismo demostrado con sumar_areas() y sumar_perimetros()")
    print(" Sobrescritura de métodos: area(), perimetro(), __str__()")
    print(" Código siguiendo estándar PEP8")

    imprimir_separador()
    print(f"Programa finalizado - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()