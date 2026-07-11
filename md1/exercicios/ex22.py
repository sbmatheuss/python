try:
  n1 = int(input('Primeiro número: '))
  n2 = int(input('Segundo número: '))
  op = input('Operação (+, -, *, /): ')
  if op == '+':
    print(n1+n2)
  elif op == '-':
    print(n1-n2)
  elif op == '*':
    print(n1*n2)
  elif op == '/':
    print(n1/n2)
  else:
    print('Operação inválida!')
except ValueError:
  print('Digite somente números!')
except ZeroDivisionError:
  print('Erro, número divido por 0')