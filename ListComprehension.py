lista_numeros = [1, 2, 3, 4, 5]
y = []

for i in lista_numeros:
    y.append(i**2)

print(lista_numeros)
print(y)

# Com List Comprehension
# (valor_a_adicionar laco condicao)

z = [i**2 for i in lista_numeros]
print(z)

w = [i for i in lista_numeros if i%2 == 1]
print("Numeros ímpares da lista", w)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [lista_numeros for lista_numeros in fruits if "a" in lista_numeros]

print("Lista de frutas com a letra 'a'", newlist)
