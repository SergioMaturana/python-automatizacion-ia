def clasificar_temperatura(grados):
    if grados > 30:
        return "Hace calor"
    else:
        return "Temperatura normal"

print(clasificar_temperatura(35))
print(clasificar_temperatura(20))