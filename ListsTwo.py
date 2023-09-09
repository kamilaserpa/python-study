lista_numeros = [124,345,5,72,46,6,7,3,1,0]

# sorted(list) retorna a lista ordenada, não altera a lista recebida por parâmetro 
sorted(lista_numeros)
print("Lista:", lista_numeros)

lista_numeros.sort()
print("Lista ordenada:", lista_numeros)

lista_numeros.sort(reverse=True)
print("Lista ordem desc:", lista_numeros)

lista_numeros.reverse()
print("Lista ordem revertida:", lista_numeros)

lista_diversa = ["bola", "abacate", "dinheiro"]

lista_diversa.sort()
print("Lista ordem alfabetica:", lista_diversa)

lista_diversa.sort(reverse=True)
print("Lista ordem alfabetica desc:", lista_diversa)

