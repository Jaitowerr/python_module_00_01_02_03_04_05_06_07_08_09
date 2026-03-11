### *Para probar estos ejercicios ejecuta desde esta raíz `python3 main.py` y pulsa sobre la `a` para avanzar test por test.* 
---
<br><br>

# 🌿 Aprendizaje Python - Módulo 00 (42Madrid)


Este documento resume los conceptos fundamentales de Python aprendidos durante la resolución de los ejercicios del **Jardín de Python**.

#### 1. Salida de Datos: `print()`
La función `print()` muestra información en la consola.
- **Argumentos múltiples**: `print("Hola", "Mundo")` añade un espacio automáticamente entre palabras.
- **Separador personalizado**: `sep='\n'` permite cambiar el espacio por un salto de línea u otro carácter.
- **Fin de línea**: `end=''` evita que el cursor salte a la siguiente línea tras imprimir.

#### 2. Entrada de Datos: `input()`
Permite recibir texto del usuario.
- **Importante**: `input()` siempre devuelve un **String** (texto).
- Ejemplo: `nombre = input("Dime tu nombre: ")`

#### 3. Conversión de Tipos: `int()` y `float()`
Para realizar cálculos matemáticos, debemos convertir el texto de `input()` a números.
- `entero = int("10")`
- `decimal = float("10.5")`

#### 4. Estructuras de Control: `if`, `elif`, `else`
Permiten tomar decisiones en el código.
- **Sintaxis**: Es obligatorio el uso de `:` al final de la condición y la **indentación** (4 espacios).
- `elif` se usa para encadenar múltiples condiciones de forma eficiente.

#### 5. Bucles y Secuencias: `range()`
Genera una secuencia de números.
- `range(inicio, fin, paso)`: El `fin` no está incluido.
- `range(1, 5)` genera: 1, 2, 3, 4.
- Para contar hacia atrás, el paso debe ser negativo: `range(10, 0, -1)`.

#### 6. Funciones: `def` y Anotaciones
Las funciones agrupan código reutilizable.
- **Firma con tipos**: `def mi_funcion(param: str) -> None:` indica que espera un texto y no devuelve nada.
- **Recursión**: Una función que se llama a sí misma. Requiere siempre una **condición de parada** para evitar bucles infinitos.
- **Helper functions**: Funciones auxiliares que ayudan a la función principal (común en recursión).

#### 7. Estilo y Normas (PEP 8 / Flake8)
Para que el código sea profesional y pase los correctores de 42:
- **Indentación**: Siempre 4 espacios (no usar Tabs).
- **Espacios en blanco**: Dos líneas en blanco entre funciones. Una línea en blanco al final del archivo.
- **Operadores**: Un espacio alrededor de `=`, `+`, `<`, etc. (excepto en parámetros por defecto).

#### 8. Métodos de String
- `.capitalize()`: Convierte la primera letra en mayúscula y el resto en minúscula.
