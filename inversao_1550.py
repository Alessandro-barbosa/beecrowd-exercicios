def inver(num):  # botao inverter
    x = reversed(num)
    x = ''.join(x)
    return int(x)


def add(num):  # botao adicionar 1
    x = num + 1
    return int(x)


tam = input()
for j in range(int(tam)):
    m, i = [int(x) for x in input().split()]
    grafo = {
        m: i
    }

for key, value in grafo.items():
