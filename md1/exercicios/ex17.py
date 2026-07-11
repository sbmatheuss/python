try:
  number = int(input('Digite um número: '))
  divi = 100 / number
  print(f'Resultado: {divi}')
except ZeroDivisionError:
  print(f'{ZeroDivisionError} divisão por zero não é permitida' )
finally:
  print('Programa Encerrado!')