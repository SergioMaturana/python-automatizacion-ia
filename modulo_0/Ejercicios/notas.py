# Ejercicio: Escribe un script que, a partir de una variable "nota"
# (un número entre 0 y 10), imprima la calificación correspondiente
# usando un f-string:
#
# nota >= 9 -> "Sobresaliente"
# nota >= 7 -> "Notable"
# nota >= 5 -> "Aprobado"
# cualquier otro caso -> "Suspenso"
#
# El mensaje final debe mostrar tanto la nota como la calificación,
# por ejemplo: "Con un 8 has sacado: Notable"

nota = 6

if nota >= 9:
    calificacion = "Sobresaliente"
elif nota >= 7:
    calificacion = "Notable"
elif nota >= 5:
    calificacion = "Aprobado"
else:
    calificacion = "Suspenso"

print(f"Con un {nota} has sacado: {calificacion}")