lista_frutas = ["manga", "acerola", "morango", "abacate", "kiwi", "caju"]

print("Lista ordenada:")

print(lista_frutas[0])
lista_frutas.sort()

for item in lista_frutas:
    print(item)

print("----------")

lista_frutas.append("limao")

print(lista_frutas)

print("----------")

if "manga" in lista_frutas:
    print("Manga está na lista")
else:
    print("Manga NÃO está na lista")

print("----------")

del lista_frutas[4:] # remove o índice 4 e os próximos
print(lista_frutas)

del lista_frutas[2] # remove o índice 2
print(lista_frutas)

del lista_frutas[:] # remove tudo

print("----------")
lista_numeros = []
lista_numeros.append(4)
lista_numeros.append(6)
lista_numeros.append(8)

print(lista_numeros)
print(len(lista_numeros))
