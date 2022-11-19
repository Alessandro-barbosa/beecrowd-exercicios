# # busca em largura
# grafo = {
#     0: [1, 2, 3],
#     1: [4, 5],
#     2: [4, 5],
#     3: [4, 6],
#     4: [7],
#     5: [7],
#     7: []
# }
# lista = set()
# for key, values in grafo.items():
#     lista.update(values)
#     print(lista)
# 1 2 3 4 5 6 7
# s = int(input())
# c = {
#     'a': [1, 1],
#     'b': [8, 6],
#     'c': [6, 8],
#     'd': [1, 3]
# }
# x = 0
# y = 1
# soma = set()
# for ki, vi in c.items():
#     menordist = 500000
#     for kj, vj in c.items():
#         dist = ((vj[x] - vi[x])**2 + (vj[y] - vi[y])**2) ** (1/2)
#         if dist < menordist and dist != 0:
#             menordist = dist
#         print(f"{dist:.2f}", end=" ")
#     soma.add(menordist)
#     print()
# print(f"{sum(soma):.2f}")
for i in range(2, -5, -1):
    print(i, end=", ")