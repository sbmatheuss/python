while True: 
  try: 
    number = int(input('Digite um número: '))
    break
  except (ValueError):
    print(f'Tente novamente')
  finally: 
    print(f'Obrigado, volte sempre!')

