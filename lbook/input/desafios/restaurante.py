# Converte para int para poder comparar com 8
pessoas = int(input('Quantas pessoas estão em seu grupo para jantar? '))
print(pessoas)

# Grupos com mais de 8 pessoas precisam esperar
if pessoas > 8:
    print('Aguardar uma mesa')
else:
    print('Mesa pronta')
