numeros = [1, 2, 3, 4, 5, 6, 7, 8]

pares = [n for n in numeros if n % 2 == 0]

print(numeros)
print(pares)

dobles_de_pares = [n * 2 for n in numeros if n % 2 == 0]
print(dobles_de_pares)