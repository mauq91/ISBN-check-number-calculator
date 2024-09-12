# Cálculo de Número de Verificación (Check Number) para ISBN en Python

Este script en Python calcula el número de verificación (check number) para un ISBN utilizando el algoritmo de módulo 11. Toma una lista de dígitos de un ISBN y otra lista de multiplicadores para calcular el número de verificación necesario para que la suma sea divisible por 11.

## Descripción del Código

- El script toma dos listas: una con los dígitos del ISBN y otra con una tabla de multiplicadores.
- Calcula el producto de cada dígito del ISBN por su correspondiente multiplicador y suma los resultados.
- Luego, ajusta la suma total para que sea divisible por 11, incrementando la variable `check_num` hasta que la condición se cumpla.

## Características

- **Cálculo de la suma total**: Calcula el producto de cada dígito del ISBN con su correspondiente valor en la tabla de multiplicadores.
- **Determinación del número de verificación**: Encuentra el número de verificación que permite que la suma total sea divisible por 11.
- **Salida clara**: Muestra la suma total y el número de verificación correspondiente.

## Ejemplo de Uso

El código se puede ejecutar directamente y calculará el número de verificación para cualquier ISBN ingresado en la lista.

### Ejemplo:
```python
isbn = [1, 5, 8, 7, 1, 4, 3, 7, 3]
tabla = [10, 9, 8, 7, 6, 5, 4, 3, 2]

# Salida:
# Suma total es: 233
# Check number correspondiente es: 9
