try:
  nome = str(input('Qual seu nome completo:  '))
  maiusc = nome.upper()
  minusc = nome.lower()
  quanti_letras = len(nome)
  print(f'{maiusc}, {minusc}, {quanti_letras}')
except:
  print({nome})