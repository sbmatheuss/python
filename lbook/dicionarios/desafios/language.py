favorite_languages = {
    'jen': 'python',
    'serah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}


pessoas = ['jen', 'serah', 'matheus', 'bruno']


for pessoa in pessoas:
    if pessoa in favorite_languages:
        print(f'{pessoa.title()}, Agradeço por responder')
    else:
        print(f'{pessoa.title()}, Te convido a responder a nossa enquete')

