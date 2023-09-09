import random

# Força a seleção do memso número
# random.seed(1)
numero = random.randint(0, 10)

print(numero)

lista = [6,45,9]
numero_da_lista = random.choice(lista)
print(numero_da_lista)
