nota = int(input('Digite sua nota: '))
if nota >= 6:
  print('Aprovado')
  if nota >= 9:
    print('Com louvor')
elif nota < 6:
    if nota >= 4:
      print('De exame')
    print('Reprovado')