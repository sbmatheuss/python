# Listas dentro de Listas
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matriz[1])
print(matriz[1][2])

# Percorrendo a matriz
for linha in matriz:
    for valor in linha:
        print(valor, end=" ")

# Dicionários dentro de dicionários
aluno = {
    "nome": "Ana",
    "endereco": {
        "cidade": "Salvador",
        "estado": "BA"
    }
}

print(aluno["endereco"]["cidade"])


