planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(planeta_anao)

print('===========================================================')

qtde_p = len(planeta_anao)
print(qtde_p)

print('===========================================================')

print('Eris' not in planeta_anao)

print('===========================================================')

for astro in planeta_anao:
    print(astro.upper())

print('===========================================================')

astros = ['Lua', 'Vênus', 'Sirius', 'Marte', 'Lua']
print('Lista:', astros)
astrosSet = set(astros)
print('Conjunto:', astrosSet)

print('===========================================================')

p1 = {'Terra', 'Vênus', 'Mercúrio', 'Marte'}
p2 = {'Terra', 'Vênus', 'Mercúrio', 'Marte', 'Saturno'}
print(p1 != p2)

print('===========================================================')

p1 = {'Terra', 'Vênus', 'Mercúrio', 'Marte'}
p2 = {'Terra', 'Vênus', 'Mercúrio', 'Marte', 'Saturno'}
p1 | p2 # também da para escrever p1.union(p2)

print('===========================================================')

