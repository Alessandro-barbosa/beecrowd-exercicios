while True:
    lista = input().split(" ")
    contj = 0
    if len(lista) == 1:
        break
    player = 1
    flag = 0
    tam = len(lista)
    # 5 1 5 3 4 2 / 1 3 5 4 2 / 1 3 4 5 2 / 1 3 4 5 2 / 1 3 4 2 5 /1 3 2 4 5 / 1 2 3 4 5
    while flag != len(lista) - 1:  # 0 1 2 3 4 5
        flag = 0
        for i in range(1, len(lista)):
            if i < tam - 1:
                if lista[i] > lista[i + 1]:
                    temp = lista[i]
                    lista[i] = lista[i + 1]
                    lista[i + 1] = temp
                    i = i - 1
                    player += 1
        flag = len(lista) - 1
    if player % 2 == 0:
        print("Marcelo")
    else:
        print("Carlos")
