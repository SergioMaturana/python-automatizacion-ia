#Escribe una función describir_persona(nombre, edad) que:

#Devuelva un string usando f-string: "X tiene Y años"
#Si edad < 18, añada " (menor de edad)" al final

#Pruébala con un par de valores.

def describir_persona(nombre, edad):
    if edad < 18:
        menor = " (menor de edad)"
    else:
        menor = ""
    return f"{nombre} tiene {edad} años{menor}"

if __name__ == "__main__":
    print(describir_persona("Sergio", 22))
    print(describir_persona("Pedro", 16))