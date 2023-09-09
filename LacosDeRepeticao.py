
# LAÇOS DE REPETIÇÃO
x = 1
while x < 10:
    print("while", x)
    x += 1

lista_numeros = [1,2,3,4,5]
lista_strings = ["ola", "viagem", "prova"]
lista_multipla = [0, "ola", "biscoito", 9.89, True]

for numero in lista_numeros:
    print("for", numero)

for var in lista_multipla:
    print("outro for", var)

for i in range(10): # range inicia no Zero
    print("range() inicia em zero:", i)

for i in range(10, 20): # inicia em 10 até (20-1)
    print("range(primeiro_numero, ultimo + 1: ", i)

for i in range(10, 20, 2): # inicia em 10 até (20-1)
    print("range(primeiro_numero, ultimo + 1, intervalo: ", i)
    