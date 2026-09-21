convidados = ['henrique', 'joão', 'pedro'] # lista de convidados
print(f'Bem vindo ao jantar {convidados[0]}')
print(f'Bem vindo ao jantar {convidados[1]}')
print(f'Bem vindo ao jantar {convidados[2]}')
print(f'O convidado {convidados[1]} não irá comparecer ao jantar')
print(f'Senhores convidados, solicitei uma mesa maior')

del convidados[1] # remove o segundo convidado da lista
convidados.insert(1, 'Matheus') # insere um novo convidado na lista
print(convidados)
print(f'Bem vindo ao jantar senhor {convidados[0]}')
print(f'Deguste do nosso jantar senhor {convidados[1]}')
print(f'Seja bem vindo senhor {convidados[2]}')

convidados.insert(0, 'kaik') # acrescente um novo convidado a lista
convidados.insert(1, 'leo')# acrescente um novo convidado a lista
convidados.append('bruno')# acrescente um novo convidado a lista

print(f'Bem vindo ao jantar sr {convidados[0]}')
print(f'Bem vindo ao jantar sr {convidados[1]}')
print(f'Bem vindo ao jantar sr {convidados[5]}')

print(f'Comunicado: a nova mesa solicitada tem espaço somente para 2 lugares')
print(convidados)

# sempre que o pop() remove um convidado da lista, a cada chamada o total
# de convidados muda, exemplo: na primeira chamada abaixo, o total da lista é
# de 5 convidados, porém quando executa o pop() novamente, o total muda para 4

convidados.pop(0) # remove um convidado da lista
convidados.pop(1) # remove um convidado da lista
convidados.pop(2) # remove um convidado da lista 
convidados.pop(0) # remove um convidado da lista

print(convidados)
print(f'Bem vindo novamente sr {convidados[0]}')
print(f'Bem vindo novamente sr {convidados[1]}')

# nesse caso o del também remove e muda o total da lista a cada nova chamada
del convidados[0] # remove da lista
del convidados[0] # remove da lista

print(convidados) # retorna a lista vazia


