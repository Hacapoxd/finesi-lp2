
cadena = input("Introduce una cadena de texto: ")
cadena_invertida = " "

for i in range(len(cadena) - 1, -1, -1):
    cadena_invertida += cadena[i]

print(cadena_invertida)
