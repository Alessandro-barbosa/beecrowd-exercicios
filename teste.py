
while True:
    i = 0
    j = 1
    lista_num = set()
    try:
        n, m = [int(x) for x in input().split()]
        for numero in range(n, m + 1):
            while i != j:

        print(lista_num)
        possibilidades = abs(len(lista_num) - (m-n))
        print(possibilidades)
    except EOFError:
        break

