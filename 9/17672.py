f = open('txt_17672')
c = 0
for i in f:
    a = [int(x) for x in i.split()]
    a = sorted(a)
    if a[0] + a[3] < a[1] + a[2]:
        c += 1
print(c)

