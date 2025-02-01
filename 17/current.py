f = open('17_17680.txt')
a = [int(x) for x in f]

mn = []
for i in a:
    if int(i) > 0:
        if int(i) % 41 == 0:
            mn.append(i)
mn = min(mn)

p = []
for i in range(len(a) - 1):
    k = [a[i], a[i+1]]
    c = k[0] + k[1]
    k_usl = [x for x in k if k[0] != k[1]]
    if len(k_usl) > 0:
        if abs(k[0] - k[1]) % mn == 0:
            p.append(c)
print(len(p), max(p))






