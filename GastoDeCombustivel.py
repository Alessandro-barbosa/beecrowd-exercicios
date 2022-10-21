lista_notas = [100, 50, 20, 10, 5, 2, 1]
valor = int(input())
for i in lista_notas:
    y = valor // i
    j = i
    j = str(j)
    valor = valor % i
    print(f"{y} notas(s) de R$ {j},00")
