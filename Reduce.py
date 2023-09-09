# Função reduce
# Recebe uma lista e retorna um único valor
from functools import reduce

lista = [1,3,5,10,20]

def soma(x,y):
    return x + y

soma_lista = reduce(soma, lista)

print(soma_lista)
