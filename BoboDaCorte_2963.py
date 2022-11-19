c = int(input())
aux = 0
maior = 0
primeiro = 0
for i in range(c):
    aux = int(input())
    if i == 0:
        primeiro = aux
    if aux > maior:
        maior = aux
if primeiro >= maior:
    print("S")
else:
    print("N")
