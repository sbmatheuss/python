import pprint
printer = pprint.PrettyPrinter()

lst = [                                  # camada externa: repete o "meio" 5 vezes
    [                                    # camada meio: repete a "interna" 5 vezes
        [num for num in range(5)]       # camada interna: gera [0,1,2,3,4]
        for _ in range(5)
    ]
    for _ in range(5)
]
printer.pprint(lst)