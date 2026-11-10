# int() converte o texto digitado em número para poder fazer contas
numero = int(input('Qual o número? '))

# % devolve o resto da divisão: resto 0 significa que é múltiplo
if numero % 10 == 0:
    print('É múltiplo de 10')
else:
    print('Não é múltiplo de 10')
