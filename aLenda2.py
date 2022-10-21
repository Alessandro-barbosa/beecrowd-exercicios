def teste(lista, listsize, index):
    i = index
    Lista = []

    while i < listsize + index:
        Lista.append(lista[(i % listsize)])
        i = i + 1
    return Lista

entrada = int(input())

for i in range(entrada):

    a, b = input().split()
    soldados = int(a)
    intervalo = int(b)
    a = []

    for x in range(1, soldados + 1):
        a.append(x)

    n = len(a)

    while len(a) > 1:
        a = teste(a, len(a), intervalo - 1)
        a.pop(0)
    aux = a[0]
    print(f"Case {i+1}: {aux}")
