num = int(input())
for i in range(num):
    if num == 0:
        break
    print(num % 10, end="")
    num = num // 10
print("")
