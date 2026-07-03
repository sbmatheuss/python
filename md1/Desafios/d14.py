# Aumento de salário

sal = float(input('Qual o salário? R$ '))
percentual = float(input('Qual a porcentagem de aumento?% '))
aumento = sal * (percentual / 100)
novo_sal = sal + aumento

print(f'Novo salário com aumento: R${novo_sal}')    