# Ejercicio: Dada la lista de diccionarios:
# productos = [
#     {"nombre": "Teclado", "precio": 25},
#     {"nombre": "Ratón", "precio": 15},
#     {"nombre": "Monitor", "precio": 180},
#     {"nombre": "Webcam", "precio": 40},
# ]
#
# - Recorre la lista con un for
# - Para cada producto, imprime su nombre y precio
# - Si el precio es mayor de 50, imprime también "(producto caro)"
#   junto al nombre y precio

productos = [
    {"nombre": "Teclado", "precio": 25},
    {"nombre": "Ratón", "precio": 15},
    {"nombre": "Monitor", "precio": 180},
    {"nombre": "Webcam", "precio": 40},
]

for p in productos:
    if p["precio"] > 50:
        print(p["nombre"], p["precio"], "(producto caro)")
    else:
        print(p["nombre"], p["precio"])