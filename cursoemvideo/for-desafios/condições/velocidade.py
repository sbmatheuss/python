velocidade = int(input('Qual a velocidade do carro? '))
valor_km = 7

if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * valor_km
    print(f'VOCÊ FOI MULTADO: {velocidade}Km/h')
    print(f'Valor da MULTA: R${multa:2}')
else:
    print('Você está dentro do limite de Velocidade')