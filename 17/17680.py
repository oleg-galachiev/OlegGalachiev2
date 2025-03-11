f = open('17_17680.txt')
a = [int(x) for x in f]

mn = []
for i in a:
    if str(i)[0] not in ['-','0']:
        if i % 41 == 0:
            mn.append(i)
mn = min(mn)



p = []
for i in range(len(a) - 1):
    k = [a[i], a[i+1]]
    if k[0] != k[1]:
        if abs(k[0]-k[1]) % mn == 0:
            p.append(k[0]+k[1])
print(max(p),len(p))
