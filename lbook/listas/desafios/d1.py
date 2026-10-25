convidados = ['henrique', 'joão', 'pedro'] # lista de convidados

for convidado in convidados: # convida todos da lista, sem precisar de índice
    print(f'Bem vindo ao jantar {convidado.title()}')

# um convidado não poderá comparecer e será substituído
ausente = convidados[1]
print(f'\nO convidado {ausente.title()} não irá comparecer ao jantar')
convidados[1] = 'matheus' # substitui o convidado ausente na mesma posição

for convidado in convidados: # envia os convites novamente com a lista atualizada
    print(f'Bem vindo ao jantar senhor {convidado.title()}')

print('\nSenhores convidados, encontrei uma mesa maior!')
convidados.insert(0, 'kaik') # acrescenta um convidado no início da lista
convidados.insert(len(convidados) // 2, 'leo') # acrescenta um convidado no meio da lista
convidados.append('bruno') # acrescenta um convidado no final da lista

for convidado in convidados: # agora todos os 6 convidados recebem o convite
    print(f'Bem vindo ao jantar sr {convidado.title()}')

print('\nComunicado: a nova mesa tem espaço somente para 2 lugares')

# enquanto houver mais de 2 convidados, o pop() remove o último da lista
# e devolve o nome removido, que fica guardado na variável removido
while len(convidados) > 2:
    removido = convidados.pop()
    print(f'Desculpe {removido.title()}, não teremos lugar para você no jantar')

for convidado in convidados: # avisa os 2 convidados que continuam na lista
    print(f'Bem vindo novamente sr {convidado.title()}, você continua convidado')

# o del remove o elemento da posição 0; como a lista "anda" a cada remoção,
# a posição 0 sempre aponta para o próximo convidado
while convidados:
    del convidados[0]

print(convidados) # retorna a lista vazia
