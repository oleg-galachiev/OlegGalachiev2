p = []
for n in range(1,1000):
    b = bin(n)[2:]
    b = b[1:]
    if b.count('1') % 2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '0'
    r = int(b, 2)
    if r < 450:
        p.append(r)
print(max(p))