
# STRING
k = "Kamila"
s = "Serpa"

concatenacao = k + " " + s
print("Concatenação:", concatenacao)

tamanho = len(concatenacao)
print("Tamanho da string:", tamanho)

print(k[0])
print(k[1])
print(k[2])
# print(k[10]) # IndexError: string index out of range

print("k[0:4] do índice 0 (incluindo) até o 4 (excluindo) ->", k[0:4]) # Kami
print(s[2:4])

print("string.capitalize ->", k.capitalize())
print("string.upper ->", k.upper())
print("string.lower ->", k.lower())
print("string.strip (remove espaços em branco no início e final) ->", "  teste\n".strip())

print("string.strip (remove caracteres selecionados) ->", ",,,  !teste\n.jpg".strip(" !,.jpg"))

print("A variável continua com o valor inicial pois não houve atribuição ->", k)

minha_string = "O rato roeu a roupa do rei de Roma"
minha_lista = minha_string.split("r")
print("Removeu a letra escolhida para a separação, menos o R maiúsculo (pois é case sensitive):", minha_lista)

busca_rei = minha_string.find("rei")
print("Índice da palavra 'rei'(find):", busca_rei)  # 23

print("Imprime o índice de 'rei' até o final: 'minha_string[busca_rei:]' :", minha_string[busca_rei:])

busca_rainha = minha_string.find("rainha")
print("Índice da palavra não encontrada retorna -1:", busca_rainha)

print(minha_string.replace("rei", "rainha"))

print("################")
