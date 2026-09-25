# cria uma lista com quadrado de cada número (no caso de até 10), pois 11 n retorna
quadrados = [value**2 for value in range(1,11)] 
print(quadrados) # exibe a lista dos quadrados dos números

# cria uma lista com o dobro de cada número
dobro = [value*2 for value in range(1,9)]
print(dobro) 

# cria tabuada de 7
tabuada = [value*7 for value in range(1,11)]
print(tabuada)

# retorne apenas os números pares (mexe no range)
pares = [ value for value in range(2, 21, 2)]
print(pares)

# contagem regressiva
regressiva = [value for value in range(10, 0, -1)]
print(regressiva)