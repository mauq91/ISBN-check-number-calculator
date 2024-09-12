#ISBN - 10 Checknum calculator

isbn = [1, 5, 8, 7, 1, 4, 3, 7, 3]
tabla = [10, 9, 8, 7, 6, 5, 4, 3, 2]

# Sumar productos de cada elemento de las listas 'isbn' y 'tabla'
suma_total = sum(isbn[i] * tabla[i] for i in range(len(isbn)))
print(f"Suma total es: {suma_total}")

# Inicialización de la variable Checknum
check_num = 0

# Ajustar suma para que sea divisible por 11
while suma_total % 11 != 0:
    suma_total += 1
    check_num += 1

print(f"Check number correspondiente es: {check_num}")
