# Ejercicio: Escribe una función describir_persona(nombre, edad) que:
#
# - Devuelva un string usando f-string: "X tiene Y años"
# - Si edad < 18, añada " (menor de edad)" al final
#
# Pruébala con dos valores distintos.

def describir_persona(nombre, edad):
    respuesta = f"{nombre} tiene {edad} años"
    if edad < 18:
        return respuesta + " (menor de edad)"
    else:
        return respuesta

print(describir_persona("Piter", 20))
print(describir_persona("Mirlo", 15))