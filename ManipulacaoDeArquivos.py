
# MANIPULAÇÃO DE ARQUIVOS

# open(file, mode)
# Modes: 
#   "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#   "a" - Append - Opens a file for appending, creates the file if it does not exist
#   "w" - Write - Opens a file for writing, creates the file if it does not exist
#   "x" - Create - Creates the specified file, returns an error if the file exist

arquivo = open("arquivo.txt", "w") # abre arquivo apagando seu conteúdo, caso não exista cria o arquivo
arquivo.write("Esse é o meu arquivo gerado via linha de código. 1 \nEsse é o meu arquivo gerado via linha de código. 2 \nEsse é o meu arquivo gerado via linha de código. 3 \n")
arquivo.close()

arquivo2 = open("arquivo2.txt", "w") # abre arquivo apagando seu conteúdo, caso não exista cria o arquivo
arquivo2.write("Esse é o meu segundo arquivo gerado via linha de código.\n")
arquivo2.close()

arquivo = open("arquivo.txt", "a") # abre arquivo, mantém o conteúdo atual e adiciona ao final o .write
arquivo.write("Adicionando conteúdo ao meu arquivo gerado via linha de código.\n")
arquivo.close()


arquivo = open("arquivo.txt")

texto_completo = arquivo.read() # lê arquivo completo
print(".read():", texto_completo)

linhas = arquivo.readlines() # lê arquivo e armazena em uma linha
print("readlines():", linhas)

# for linha in linhas:
#     print(linha)

