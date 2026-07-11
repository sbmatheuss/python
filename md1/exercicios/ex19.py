try:
  n1 = int(input('Primeiro número: '))
  n2 = int(input('Segundo número: '))
  divi = n1 / n2
  print(f'Resultado: {divi}')
except ZeroDivisionError:
  print(f'{ZeroDivisionError} número divido por zero')
except ValueError:
  print(f'{ValueError} não é um número!')