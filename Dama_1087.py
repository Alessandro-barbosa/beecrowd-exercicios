a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if a == c and b == d:
    print(0)
elif a+1 == c or a-1 == c or b+1 == d or b-1 == d:
    print(1)
else:
    try:
        for i in range(8):
            for y in range(8):
                if a == c or b == d:
                    print(1)
    except:
        l = 2
# if():


