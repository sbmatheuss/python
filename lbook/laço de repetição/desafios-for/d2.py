# se o valor inicial não for informado, o valor padrão é zero (0)
# se o passo não for informado, o padrão é 1 
for number in range(10, 0, -1): # percorre em ordem decrescente de 10 a 1
    print(number)

squares = []
for value in range(1,11):
     square = value**2
     squares.append(square)
print(squares)
