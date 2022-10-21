a = int(input())
for i in range(a):
    enter = input()
    number = [int(temp)for temp in enter.split() if temp.isdigit()]
    number = str(number)
    aux = "".join(number)
    print(aux)
