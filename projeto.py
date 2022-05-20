def vinteUm(valor):
    lista = []
    for c1 in range(1, valor + 1):
        for c2 in range(0, valor + 1):
            for c3 in range(0, valor + 1):
                for c4 in range(0, valor + 1):
                    if c1 + c2 + c3 + c4 == 21:
                        lista.append([c1, c2, c3, c4])
    for c1 in lista:
        for c2 in c1:
            print(c2, end='')
        print('')


maxDigt = int(input('Digite o dígito máximo: '))
vinteUm(maxDigt)
