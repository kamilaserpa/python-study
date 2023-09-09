# Em Python, dicionários são arrays associativos, ou seja, um determinado valor passa a ser vinculado a uma chave. Exemplo:

dicionario_sites = {"Diego": "diegomariano.com"}

# No dicionário acima, a chave "Diego" foi vinculado ao valor "diegomariano.com". Assim, para imprimir o valor chame:

print(dicionario_sites['Diego'])
# Sera impresso "diegomariano.com


# Se o dicionário tiver vários elementos, você pode usar laços para imprimi-los:

dicionario_sites = {"Diego": "diegomariano.com", "Google": "google.com", "Udemy": "udemy.com"}
 
for chave in dicionario_sites:
    print(dicionario_sites[chave])

print("--------------------------------")

meu_dicionario = {"A": "ameixa", "B": "bola", "C" : "cachorro"}
print("meu_dicionario['A']:", meu_dicionario["A"])

for chave in meu_dicionario:
    print(chave + " -> " + meu_dicionario[chave])

print("--------------------------------")

for i in meu_dicionario.items():
    print("items:", i) # items: ('A', 'ameixa') ...

print("--------------------------------")

for k in meu_dicionario.keys():
    print("keys:", k) # keys: A ...

print("--------------------------------")

for v in meu_dicionario.values():
    print("values:", v) # values: ameixa ...