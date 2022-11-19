dist_final = 12
while True:
    try:
        d, vf, vg = [int(x) for x in input().strip().split(' ')]
        h = (dist_final**2) + (d ** 2)
        h = h**(1/2)
        temp_vg = (h/vg)
        temp_vf = (dist_final/vf)
        print("S" if temp_vg <= temp_vf else "N")
    except EOFError:
        break
,