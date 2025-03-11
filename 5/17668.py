p = []
for n in range(28,1000):
    b = bin(n)[2:]
    if b.count('1') % 2 == 0:
        b = '10' + b[2:] + '0'
    else:
        b = '11' + b[2:] + '1'
    r = int(b,2)
    p.append(r)
print(min(p))