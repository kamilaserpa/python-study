# Função Enumerate

lista_frutas = ["abacate", "bola", "laranja", "caju"]

for i in range(len(lista_frutas)):
    print(i, lista_frutas[i])

for i, fruta in enumerate(lista_frutas):
    print(i, fruta)
    