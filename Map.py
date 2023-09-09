# Função map
# Aplica uma função para cada elemento da lista

def dobro(x):
    return x * 2

valores = [1,2,3,4,5]
valores_dobrados = map(dobro, valores)

# Para printar ou convertemos para lista
lista_dobro = list(valores_dobrados)
print(lista_dobro) # [2, 4, 6, 8, 10]

# ou fazemos um laço for
# for v in valores_dobrados:
#     print(v)


