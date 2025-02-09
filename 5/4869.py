p = []
for n in range(2,10000):
    b = bin(n)[2:]
    c1 = 0
    c0 = 0
    for i in range(len(b)):
        if (i+1) % 2 == 0 and b[i] == '1':
            c1 += 1
        if (i+1) % 2 == 1 and b[i] == '0':
            c0 += 1
    res = abs(c1-c0)
    print(n,res)
    if res == 5:
        p.append(n)
print(min(p))
