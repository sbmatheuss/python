senha_correta = 'Python123'

while True:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print('Acesso liberado')
        break
    print('Senha incorreta, tente novamente')
    
print('Programa encerrado.')