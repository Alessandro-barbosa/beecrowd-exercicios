a, b = input().split()
c, d = input().split()
total = (float(a) - float(c)) ** 2 + (float(b) - float(d))**2
total = total ** (1/2)
print(f"{total:.4f}")