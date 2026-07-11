try:
  arquivo = open('dados.txt', 'r')
  print(arquivo.read())
except FileNotFoundError:
  print(f'{FileNotFoundError} Arquivo não encontrado')  