

numeros = [7, 3, 8, 1]
crescente = sorted(numeros) # criou uma nova lista com os mesmos elementos da original e retornou em ordem crescente
decrescente = sorted(numeros, reverse=True) # criou uma nova lista com os mesmos elementos da original e retornou em ordem decrescent
print(crescente)
print(decrescente)

# sorted() cria uma nova lista com os mesmo elementos da original com possibilidade de alteração
# mantendo a lista original intacta

# sort() -> ordena a lista EXISTENTE,  não retorna nada (retorna NONE)

nomes = ['Matheus', 'Thiago', 'Kauan']
resultado = nomes.sort()
print(nomes)
print(resultado)
