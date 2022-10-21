while True:
    try:
        x, y = [int(i) for i in input().split()]
        final = abs(x-y)
        print(final)
    except EOFError:
        break