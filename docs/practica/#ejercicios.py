#ejercicios

lista1 = [4, 3, 6, 5, 4]
print(lista1)

lista2 = lista1.copy()

lista2.reverse()

print(lista2)

if lista1 == lista2:
    print("Las listas son iguales.")
else:
    print("Las listas no son iguales.")