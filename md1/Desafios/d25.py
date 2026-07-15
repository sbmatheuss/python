number = int(input('Digite um número: '))
if number >= 0:
  print('Positivo')
  if number % 2 == 0:
    print('NÚMERO PAR')
  else:
    print('NÚMERO ÍMPAR')
else:
  print('NEGATIVO')
  