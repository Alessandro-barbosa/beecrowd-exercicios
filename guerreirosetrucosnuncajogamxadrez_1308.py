import math

while True:
    try:
        x = int(input())
        a = int(((math.sqrt(1 + 8 * x) - 1) / 2))
        print(a)
    except EOFError:
        break

# x = int(input())
# contador_linha = 0
# for i in range(1, x + 1):
#     if x >= i:
#         x -= i
#         contador_linha += 1
#     else:
#         break
# print(contador_linha)
