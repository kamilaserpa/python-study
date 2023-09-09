# -*- coding: utf-8 -*-

# Comentario
print("Oi python, boraaa!")

"""
Comentário de
muitas
linhas
"""
print("Vamos aprender rápido!")

print("######## OPERAÇÕES MATEMÁTICAS ########")

print("4 + 2 =", 4 + 2)
print("4 - 2 =",4 - 2)
print("40 / 2 =", 40 / 2)
print("5 * 2 =", 5 * 2)

print("2 elevado a 3 =", 2 ** 3) # exponencial
print("Módulo de 10 % 3 =", 10 % 3) # módulo ou resto da divisão

# VARIÁVEIS E TIPOS DE DADOS
# Não pode ter caracteres especiais ou espaços. É case sensitive.

print("######## OPERADORES LÓGICOS ########")

x = 3
y = 3
z = 3

print("x é igual a y?", x == y)

soma = x + y
print("x + y =", soma)

print("x maior que y?", x > y)

print("AND: x == y and x == z ?", x == y and x == z)

z = 5
print("AND: x == y and x == z ?", x == y and x == z)

print("OR: x == y or x == z ?", x == y or x == z)
print("OR: x == y or x == z and z == y ?", x == y or x == z and z == y)

print("######## OPERADOR CONDICIONAL ########")

a = 23
b = 43
if a > b:
    print("a é maior que b.")
elif a == b:
    print("a e b são iguais.")
elif a < b:
    print("a é menor que b.")
else:
    print("Não sei...")

# TUDO É OBJETO
""" Orientado a Objeto.
objeto.propriedade
objeto.metodo()"""
