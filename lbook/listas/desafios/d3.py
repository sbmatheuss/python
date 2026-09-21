paises = ['Itália', 'Paraguai', 'Canadá', 'Chile', 'Japão', 'China']

print(paises[0]) # retorna o primeiro elemento da lista

paises[0] = 'México' # modifica o primeiro elemento da lista
print(paises)

paises.append('Espanha') # acrescente um elemento novo na lista
print(paises)

paises.insert(0, 'Alemannha')
print(paises)

del paises[0] # remove um elemento da posição 0 da lista
print(paises)

paises.pop() # remove o último elemento da lista
print(paises)

paises.remove('Paraguai') # remove o elemento pelo seu valor
print(paises)

paises.sort() # ordena os elementos da lista permanentemente
print(paises)

print(sorted(paises, reverse=True)) # ordena a reversão lista de forma temporária 

paises.reverse() # inverte a ordem original da lista
print(paises)

print(len(paises)) # retorna o tamanho da lista
