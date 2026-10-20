#  o range() para antes de chegar no fim. Para incluir o último número, 
# some 1 ao fim quando conta para cima e subtraia 1 quando conta para baixo.

for numbers in range(1,6): # efetua uma contagem de 1 a 4 (sempre termina 1 digito a menos antes do final)
    print(numbers)

numbers = list(range(1,6)) # retorna a lista de 1 a 5 (sempre termina 1 digito a menos antes do final)
print(numbers)

numbers = list(range(2,11,2)) # retorna a soma de 2 em 2 até o resultado ser alcançado em 11
print(numbers)

