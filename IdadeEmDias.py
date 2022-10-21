num = int(input())
cont_ano = 0
cont_mes = 0
cont_dias = 0
while num >= 365:
    num = num - 365
    cont_ano += 1
while num >= 30:
    num = num - 30
    cont_mes += 1
print(f"{cont_ano} ano(s)")
print(f"{cont_mes} mes(es)")
print(f"{num} dias(s)")


