lista = []
while True:
    try:
        x = 1
        while x:
            x = [str(x) for x in input().split()]
            if x == "0" and len(lista) > 0:
                print()
                break
            if x != "1" and x != "0":
                x = x.strip("Package ")
                lista.append(x)
        lista = sorted(lista)
        for i in lista:
            print(f"Package {i}")
        lista = []
    except EOFError:
        print()
        break
