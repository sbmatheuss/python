# fatiando uma lista
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # fatia a lista e exibe os 3 primeiros players.

frutas = ['pera', 'melão', 'morango', 'kiwi']
print(frutas[:-3]) #  "fatia do início até o índice −3, sem incluir o −3"

frase = ['I', '','a', 'm', '', 'J', 'a', 's', 'p', 'r', 'e', 'e', 't']
print(frase[2:10:2]) 

vogais = ['a','b','c','a','b','c','a','b','c']
print(vogais[:5:3])

matrix = [
    ['a','b','c'], # Row 0
    ['d','e','f'], # Row 1
    ['g','h','i'], # Row 2
]
print(matrix[1][1:])

games = ['overwatch', 'batman', 'GTA V']
for game in games[:2]: # percorre a lista inteira de games e fatia
    print(game.title()) 