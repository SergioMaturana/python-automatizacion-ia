persona = {"nombre": "Sergio", "edad": 22}

print(persona["profesion"])       # esto da error: KeyError

print(persona.get("profesion"))          # None (no rompe)
print(persona.get("profesion", "N/A"))   # "N/A" (valor por defecto si no existe)