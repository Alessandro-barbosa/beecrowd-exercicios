while True:
    lista_num = set()
    try:
        n, m = [int(x) for x in input().split()]
        for numero in range(n, m + 1):
            for i in range(len(str(numero))):
                letra_i = str(numero)[i]
                for j in range(i+1, len(str(numero))):
                    letra_j = str(numero)[j]
                    if letra_i == letra_j:
                        lista_num.add(numero)
        possibilidades = abs(len(lista_num) - (m-n+1))
        print(possibilidades)
    except EOFError:
        break

