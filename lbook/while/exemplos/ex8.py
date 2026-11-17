usuarios_pendentes = ['carla', 'bruno', 'ana']
usuarios_confirmados = []


#Repete enquanto ainda houver itens pendentes

while usuarios_pendentes:
    usuario = usuarios_pendentes.pop()
    print(f"Confirmando: {usuario.title()}")
    usuarios_confirmados.append(usuario)

print("\nUsuários confirmados")
for usuario in usuarios_confirmados:
    print(usuario.title())

