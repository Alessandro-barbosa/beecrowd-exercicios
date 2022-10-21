qtd = int(input())
list = [str(l) for l in input().split()]
print(list)
for i in range(len(list)):
    palavra_1 = list[i]
    contador_final = 0
    for j in range(len(palavra_1)):
        palavra_2 = list[i+1]
        contador_letra = 0
        for k in range(len(palavra_2)):
            while palavra_1[j] == palavra_2[k]:
                    j += 1
                    k += 1
                    contador_letra += 1


