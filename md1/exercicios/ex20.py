try:
  nomes = ['Ana', 'Sther', 'Bruno']
  indice = int(input('Digite um índice: '))
  print(nomes[indice])
except IndexError:
  print(f'{IndexError} Índice inválido')
except ValueError:
  print(f'{ValueError} Digite um número inteiro!')
  