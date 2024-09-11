print("cuantas letras hay en la frase?")

frase = input("escribe una frase: ")

letra = input("letra a buscar: ")

if len(letra) != 1:
    print("Por favor, introduce solo una letra.")

else:
    conteo = frase.count(letra)
    print(f"La letra '{letra}' aparece {conteo} veces en la frase.")