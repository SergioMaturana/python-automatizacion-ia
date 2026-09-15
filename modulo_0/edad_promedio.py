#Escribe una función edad_promedio(personas) que:

#Reciba la misma lista de diccionarios de antes
#Calcule la media de edad de todas las personas
#Si la lista está vacía, en vez de que el programa crashee (división por cero), capture el error con try/except y devuelva 0

#Pista: si personas está vacía, len(personas) es 0, y dividir por 0 lanza ZeroDivisionError. Completa el except y pruébalo con la lista normal y con una lista vacía [].

from resumen_personas import personas

def edad_promedio(personas):
    try:
        total = sum(p["edad"] for p in personas)
        return total / len(personas)
    except ZeroDivisionError:
        return 0

if __name__ == "__main__":
    print(edad_promedio(personas))
    print(edad_promedio([]))