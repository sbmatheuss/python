produto = float(input('Preço do produto?R$ '))
percentual = float(input('Valor do desconto:  %'))  
desconto = produto * (percentual / 100) 
preco_final = produto - desconto

print(f'Desconto: R$ {desconto}')
print(f'Preço final: R$ {preco_final}')