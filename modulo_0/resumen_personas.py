#Escribe una función resumen_personas(personas) que reciba una lista de diccionarios:
#
#personas = [
#    {"nombre": "Sergio", "edad": 22},
#    {"nombre": "Pedro", "edad": 16},
#    {"nombre": "Ana", "edad": 30},
#]
#
#Y devuelva una lista de strings, usando tu función describir_persona para cada una, mediante una list comprehension (no un for tradicional).
#
#Pista: dentro de la comprehension llamas a describir_persona(p["nombre"], p["edad"]) por cada p en personas.
#
#python
#def resumen_personas(personas):
#    return [... for p in personas]
#
#Complétala, pruébala con la lista de ejemplo (imprime el resultado), y cuando la tengas la revisamos antes de pasar a diccionarios en profundidad y sets.

from describir_persona import describir_persona

def resumen_personas(personas):
    return [describir_persona(p["nombre"], p["edad"]) for p in personas]

personas = [
    {"nombre": "Sergio", "edad": 22},
    {"nombre": "Pedro", "edad": 16},
    {"nombre": "Ana", "edad": 30},
]

if __name__ == "__main__":
    print(resumen_personas(personas))