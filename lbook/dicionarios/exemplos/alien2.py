# Dicionário com a posição e a velocidade do alien
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

# Pega o valor de 'x_position' (0), converte para texto com str() e imprime
print('Original x-position: ' + str(alien_0['x_position']))

# Define quanto o alien anda conforme a velocidade
# Como speed é 'medium', entra no elif: x_increment = 2
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# somar x_increment à x_position e mostrar a nova posição

