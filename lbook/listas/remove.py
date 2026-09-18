carros = ['BMW', 'CIVIC', 'MERCEDES']
del carros[1] # (del) remove o segundo item da lista.
print(carros)

# remove o valor da lista e ainda tem acesso ao valor removido.
motos = ['honda', 'yamaha', 'suzuki']
print(motos)
popped_motos = motos.pop(1) 
print(popped_motos)


# RESUMINDO:
# PRECISA USAR O ITEM DEPOIS DE REMOVER? USE - pop()
# QUER SOMENTE REMOVER? USE - del


# remove() -> remove pelo valor do elemento da lista, não pelo índice

bikes = ['chimano', 'bmx']
bikes.remove('chimano') # remove o elemento da lista pelo valor
print(bikes)