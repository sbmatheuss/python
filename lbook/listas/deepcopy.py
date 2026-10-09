import copy

frutas = [['Pera', 'Melancia'], 'Maçã', 'Kiwi', 'Goiaba'] # lista aninhada
print(frutas)
rasa = frutas.copy() # faz uma cópia rasa da lista original
profundo = copy.deepcopy(frutas) # faz uma cópia profunda da lista original

rasa[0].append('Uva') # acrescenta no primeiro índico um novo elemento
profundo[0].append('Laranja') # acrescenta no primeiro índice um novo elemento

print(rasa)
print(profundo)