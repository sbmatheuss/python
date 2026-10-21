from random import randint 
# importa o módulo random  

numero_sorteado = randint(0, 5) 
# sortea o número de 0 a 5

numero_user = int(input('Qual será o número sorteado entre 0 e 5? '))
# pergunta ao usuário qual o palpite do sortei

if numero_user == numero_sorteado:
    # compara se o número digitado pelo usuário é igual ao número que foi sorteado
    print(f'Parabéns, você acertou! Número sorteado: {numero_sorteado}')
elif numero_user > 5 or numero_user < 0:
    # compara se o número que o usuário digitou esta dentro do limite e
    #  é maior que 5 e menor que 0
    print('Número não permitido')
else:
    print(f'Tente novamente! Número sorteado: {numero_sorteado}')

