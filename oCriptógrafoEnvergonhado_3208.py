while True:
    try:
        x, y = [int(i) for i in input().split()]
        if x == 0:
            exit()
        primos = []
        cont = 0
        for i in range(2, x + 1):
            if i <= 5:
                if x % i == 0:
                    if cont == 2:
                        break
                    primos.append(i)
                    cont += 1
            elif i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 6 != 0:
                if x % i == 0:
                    if cont == 2:
                        break
                    primos.append(i)
                    cont += 1
        for i in primos:
            if i < y:
                print(f"BAD {i}")
                break
            else:
                print("GOOD")
                break
    except EOFError:
        break
