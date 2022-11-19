import math

while True:
    try:
        x = int(input())
        for i in range(x):
            a = int(input())
            b = int(((math.sqrt(1 + 8 * a) - 1) / 2))
            print(b)
    except EOFError:
        break
