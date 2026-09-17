# Ejercicio: Dada la lista de números:
# numeros = [3, 8, 15, 22, 7, 40, 11, 9]
#
# - Crea una lista nueva "mayores" con los números mayores que 10,
#   usando una list comprehension
# - Crea una lista nueva "duplicados" con el doble de cada número
#   de la lista original, usando un for tradicional con .append()
# - Imprime ambas listas

numeros = [3, 8, 15, 22, 7, 40, 11, 9]

mayores = [n for n in numeros if n > 10]

duplicados = []

for n in numeros:
    duplicados.append(n * 2)

print(numeros)
print(mayores)
print(duplicados)