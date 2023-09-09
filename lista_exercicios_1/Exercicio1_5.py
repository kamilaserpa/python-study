# Lista de Exercícios 1

# Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.   
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
operacao = input("Digite a operação matemática: ")

if operacao == "+":
    resultado = a + b
elif operacao == "-":
    resultado = a - b
elif operacao == "*":
    resultado = a * b
elif operacao == "/":
    resultado = a / b
else:
    print("Sinal inválido.")
 
print(resultado)