def mdc(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a

n, a, b = [int(x) for x in input().split()]
while n != 0 and a != 0 and b != 0:
    list_num = set()
    if n % a != 0:
        temp_a = ((n % a) - n)
    else:
        temp_a = n
    total_a = abs((a + (-a)) - temp_a) / a  # qtd dos multiplos de a
    if n % b != 0:
        temp_b = ((n % b) - n)
    else:
        temp_b = n
    total_b = abs((b + (-b)) - temp_b) / b  # qtd dos multiplos de b

    mdc_final = mdc(a, b)
    mmc = (a*(b/mdc_final))
    if n % mmc != 0:
        temp_mmc = ((n % mmc) - n)
    else:
        temp_mmc = n
    temp_mcc = abs((mmc + (-mmc)) - temp_mmc) / mmc

    aux_final = (total_a+total_b) - temp_mcc
    print(f"{aux_final:.0f}")
    n, a, b = [int(x) for x in input().split()]
