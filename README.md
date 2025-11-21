# Figuras-Geometricas
# Taller de POO - Figuras Geométricas

## Descripción del Ejercicio
Este proyecto implementa un sistema de figuras geométricas en python utilizando los principios de programación orientada a objetos (POO): encapsulamiento, herencia y polimorfismo.

## Estructura del Proyecto
```
/TallerFigurasPOO/
│── figura_geometrica.py
│── cuadrado.py
│── rectangulo.py
│── circunferencia.py
│── main.py
└── README.md
```

## Clases Implementadas

### 1. FiguraGeometrica (Clase Base)
- **Atributos privados**: `_ancho`, `_alto`
- **Propiedades**: Getters y setters con validación (valores > 0)
- **Métodos**: 
  - `area()`: Calcula ancho * alto
  - `perimetro()`: No implementado (debe sobrescribirse)
  - `__str__()`: Representación en string

### 2. Cuadrado
- **Hereda de**: FiguraGeometrica
- **Constructor**: Recibe un solo parámetro (lado)
- **Métodos sobrescritos**:
  - `area()`: lado²
  - `perimetro()`: 4 * lado

### 3. Rectangulo
- **Hereda de**: FiguraGeometrica
- **Constructor**: Recibe ancho y alto
- **Métodos sobrescritos**:
  - `area()`: ancho * alto
  - `perimetro()`: 2 * (ancho + alto)

### 4. Circunferencia
- **Hereda de**: FiguraGeometrica
- **Constructor**: Recibe radio
- **Métodos sobrescritos**:
  - `area()`: π * radio²
  - `perimetro()`: 2 * π * radio

## Características Implementadas

**Encapsulamiento**: Atributos privados con @property y @setter  
**Validaciones**: Todos los valores deben ser > 0  
**Herencia**: Todas las figuras heredan de FiguraGeometrica  
**Polimorfismo**: Funciones `sumar_areas()` y `sumar_perimetros()`  
**PEP8**: Código siguiendo estándar de Python  

## Ejecución
```bash
python main.py
```

## Evidencia de Ejecución
<img width="1599" height="899" alt="Captura de pantalla 2025-11-20 221336" src="https://github.com/user-attachments/assets/74de69f5-1fab-49c1-badb-037a2ed663e0" />
<img width="1599" height="899" alt="Captura de pantalla 2025-11-20 221437" src="https://github.com/user-attachments/assets/26f6cd74-d014-4018-8bd4-802e57707dd2" />
<img width="1599" height="899" alt="Captura de pantalla 2025-11-20 221444" src="https://github.com/user-attachments/assets/d834570c-08ec-4ae2-9624-a77a0f7d3d74" />
<img width="1599" height="899" alt="Captura de pantalla 2025-11-20 221454" src="https://github.com/user-attachments/assets/70fb6b62-7a7b-4e91-aa6c-b42ede479313" />
<img width="1599" height="899" alt="Captura de pantalla 2025-11-20 221516" src="https://github.com/user-attachments/assets/42d9821e-ef81-4065-9fc3-25822c40b7dd" />

## Autor
[Javier Agusto Gomez]
