# Função filter
idades = [5, 12, 17, 18, 24, 32]

def maioridade(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(maioridade, idades)

for x in adults:
  print(x)
  