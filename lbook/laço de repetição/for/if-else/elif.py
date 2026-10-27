age = int(input('Qual sua idade? '))

if age < 4:
    price = 0
    print(f'Criança: Entrada Gratuita ${price} dólares')
elif age < 18:
    price = 5
    print(f'Adolescente: Valor da entrada ${price} dólares')
else:
    price = 10
    print(f'Adulto: Valor da entrada ${price} dólares')