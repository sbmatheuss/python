rios = {
    'nilo': 'egito',
    'amazonas': 'peru',
    'mississipi': 'estados unidos'
}

# laço que exibe uma frase sobre cada rio
for rio, pais in rios.items():
    if rio == 'nilo':
        print('O Nilo corre pelo Egito')
    elif rio == 'amazonas':
        print('O Amazonas corre pelo Peru')
    else:
        print('O Mississipi corre pelo Estados Unidos')

print('=================================================')

for rio in rios.keys():
    print(rio)

print('=================================================')

for rio in rios.values():
    print(rio)

print('=================================================')

