curso_python = ['Ana', 'Bruno', 'Carla', 'Ana', 'Diego'] 
curso_dados = ['Carla', 'Diego', 'Eva', 'Fábia', 'Eva']

# convert para set
python = set(curso_python)
dados = set(curso_dados)

# um set guarda cada elemento uma única vez e não tem ordem.
# a conversão elimina os repetidos

print('Alunos único em Python:', python)
print('Fazem os dois cursos:', python & dados)
print('Só fazem Python:', python - dados)
print('Total de alunos distintos:', len(python | dados))

