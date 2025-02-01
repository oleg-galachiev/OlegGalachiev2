def per(a, b):
    c = ''
    while a>=b:
        c += str(a%b)
        a //= b
    c += str(a)
    return c[::-1]



p = []
for n in range(1,10000):
    b = per(n, 9)
    for f in range(4):
        if b.count('7') == b.count('5'):
            b += b[-1]
        else:
            c = []
            for i in range(9):
                i = str(i)
                c.append([b.count(i), i])
                k = max(c)
                b += k[1]
    b = int(b,9)
    b = hex(b)[2:]
    if 'bac' in b:
        p.append(n)
print(max(p))

















