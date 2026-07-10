idade = 0
try: 
  idade = int(input('Digite sua idade: '))
  if idade < 0:
    raise ValueError
    
except (ValueError):
  if idade < 0:
    print(f'Não faz sentido!')
  else:
    print(f'Somente números são válidos!')
else:
  print(f'Você tem {idade} anos')