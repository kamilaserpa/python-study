# Função zip
# Associa duas ou mais listas

lista_numerica = [1, 2, 3, 4, 5]
lista_nomes = ["avião", "bola", "cachorro", "dinossauro", "elefante"]
lista_valores = ["R$ 500,00", "R$ 20,00", "R$ 40,00", "R$ 13,00", "R$ 21,00"]

for numero, nome, valor in zip(lista_numerica, lista_nomes, lista_valores):
    print(numero, nome, valor)

# Saída:
# 1 avião R$ 500,00
# 2 bola R$ 20,00
# 3 cachorro R$ 40,00
# 4 dinossauro R$ 13,00
# 5 elefante R$ 21,00
