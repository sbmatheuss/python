# Pega todos os numeros pares de 0 a 50

evens = [
    number                      # guarda o numero
    for number in range(52)     # percorre de 0 a 51
    if number % 2 == 0          # filtro: só passa se for par
]
print(evens)


options = ["any", "albany", "apple", "world", "hello", ""]

valid_strings = [
  string                    # guarda a string, se passar em todos os "if" abaixo
  for string in options     # percorre cada string de options
  if len(string) >= 2       # filtro 1: precisa ter 2+ caracteres (evita erro no [0]/[-1] de string vazia)
  if string[0] == "a"       # filtro 2: primeiro caractere precisa ser "a"
  if string[-1] == "y"      # filtro 3: ultimo caractere precisa ser "y"
]
# múltiplos "if" = E lógico (and): só entra na lista se passar em TODOS

print(valid_strings)

