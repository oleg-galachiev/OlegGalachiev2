p = []
for n in range(1,1000):
    b = hex(n)[2:]
    c = b.count('b')
    if c % 2 == 0:
        b = '1' + b
    else:
        b += '1'
    r = int(b, 16)
    if len(str(r)) == 2:
        p.append(n)
print(len(p))