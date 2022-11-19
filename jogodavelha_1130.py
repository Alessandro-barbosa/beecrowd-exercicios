def grundy(x):
    if x == 1:
        return True
    else:
        return grundy(x - 1)


while True:
    try:
        entrada = int(input())
        if entrada == 0:
            break
        palavra = input().upper()
        cont = 0
        for i in palavra:
            if i == "X":
                cont += 1

    except EOFError:
        break
