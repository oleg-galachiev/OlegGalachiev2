p = []
for n in range(1,1000):
    c = bin(n)[2:]
    if n % 3 == 0:
        c = '1' + c[:-2] + '11'
    else:
        c = '10' + c + '0'
    r = int(c, 2)
    if r > 999:
        if n % 2 == 0:
            p.append(r)
print(min(p))
