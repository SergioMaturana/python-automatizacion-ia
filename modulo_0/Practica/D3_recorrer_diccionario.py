persona = {"nombre": "Sergio", "edad": 22, "ciudad": "Valladolid"}

for clave, valor in persona.items():
    print(clave, valor)

for clave in persona.keys():
    print(clave)

for valor in persona.values():
    print(valor)