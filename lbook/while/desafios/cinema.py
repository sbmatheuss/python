while True:
    # guarda o texto puro para poder checar 'quit' antes de converter
    resposta = input('Qual a sua idade? (digite quit para sair) ')

    if resposta == 'quit':
        break

    idade = int(resposta)

    if idade <= 3:
        print('Entrada Gratuita')
    elif idade <= 12:
        valor_ingresso = 10
        print(f'Ingresso {valor_ingresso} doláres')
    else:
        valor_ingresso = 15
        print(f'Ingresso {valor_ingresso} doláres')
