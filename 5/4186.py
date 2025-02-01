p = []
for n in range(1,1000):
    c = bin(n)[2:]
    if n % 2 == 0:
        c = '10' + c
    else:
        c = '1' + c + '01'
    r = int(c, 2)
    if r > 441:
        p.append(n)
        break
print(p)