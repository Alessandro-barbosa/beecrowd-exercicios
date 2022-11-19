word = "abcdefghijklmnopqrstuvwxyz"
number = int(input())
for l in range(number):
    list = []
    y = input()
    y = y.replace(' ', '')
    y = y.replace(',', '')
    wordConter = 0
    for i in word:
        for j in y:
            if i == j:
                list.append(i)
    list = set(list)
    print("frase ", end="")
    if len(list) == 26:
        print("completa")
    elif len(list) >= 13:
        print("quase completa")
    else:
        print("mal elaborada")
