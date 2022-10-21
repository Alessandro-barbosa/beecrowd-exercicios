while True:
    n, b = [int(x) for x in input().split()]
    if n == 0 and b == 0:
        break
    else:
        bolas = [int(x) for x in input().split()]
        chances = set()
        for i in range(b):
            for j in range(i+1, b):
                print(bolas[i], bolas[j])
                chances.add(abs(bolas[i] - bolas[j]))
        print('Y' if len(chances) == n else 'N')


