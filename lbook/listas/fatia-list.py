# fatiando uma lista: lista[inicio:fim] -> pega de "inicio" ATÉ "fim", sem incluir "fim"
players = ['charles', 'martina', 'michael', 'florence', 'eli']
#           índice 0     1          2          3           4
print(players[0:3])  # ['charles', 'martina', 'michael'] -> índices 0, 1 e 2 (o 3 fica de fora)

# índice negativo conta de trás pra frente: -1 é o último, -2 o penúltimo...
frutas = ['pera', 'melão', 'morango', 'kiwi']
#          índice  0       1        2          3
#          negativo -4     -3       -2         -1
print(frutas[:-3])  # ['pera'] -> do início até antes do -3 ('melão')

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
