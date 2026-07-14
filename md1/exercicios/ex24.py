try:
  number = int(input('Digite um número: '))
  print(f'Número digitado {number}')
except ValueError:
  print(f'Digite um valor númerico! ')