pizzas = ['Frango', 'Mussarela', 'Calabresa', '4 queijos', 'Brigadeiro']
pizzas.append('Romeu e Julieta') # adiciona um novo sabor após o último elemento da lista
print(pizzas)
friend_pizzas = pizzas.copy() # faz a cópia da lista original

friend_pizzas.append('Picanha') # adiciona um novo sabor na cópia da lista original
print(friend_pizzas)

print('Minhas pizzas favoritas são:')
for pizza in pizzas[1:3]: 
# percorre a lista original e fatia, 
# retornando o primeiro índice e o segunda
    print(pizza.title())

print('As pizzas favoritas de meu amigo são:') 
for friend in friend_pizzas[5:]: 
# percorre a listaoriginal e fatia, 
# retornando o quinto e o último índice da cópia da lista original
    print(friend.title())







