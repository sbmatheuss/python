# cria uma lista com 4 marcas de carro
cars = ['audi', 'bmw', 'subaru', 'toyota']

# percorre a lista: a cada volta, "car" recebe o próximo item
for car in cars:
    # verifica se o carro atual é igual a 'bmw' (== compara valores)
    if car == 'bmw':
        # se for 'bmw', exibe tudo em maiúsculas -> BMW
        print(car.upper())
    # caso contrário (qualquer carro que não seja 'bmw')
    else:
        # exibe com a primeira letra maiúscula -> Audi, Subaru, Toyota
        print(car.title())
