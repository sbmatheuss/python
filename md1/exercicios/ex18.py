while True:
  try:
    number = int(input('Digite um número: '))
    print(f'Número digitado {number}')
    break
  except:
    print('Isso não é um número!')
  finally:
    print(f'Programa encerrado')