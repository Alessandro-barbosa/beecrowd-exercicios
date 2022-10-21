valor = 0
total = 0
for x in range(2):
    cod, uni, preco = input().split()
    valor = int(uni) * float(preco)
    total += valor
print(f"VALOR A PAGAR: R$ {total:.2f}")
