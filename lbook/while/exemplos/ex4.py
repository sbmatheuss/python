var = 20 # valor inicial
while (var > 0): # enquanto var for maior que 0 será executado o código abaixo
    print(f'O valor de var é {var}' )
    var -= 1 # pega o valor de e subtrai por 1
    if (var == 11): # se var for igual a 11 o programa encerra
        break # encerra o loop
print('Loop interrompido no valor 11')