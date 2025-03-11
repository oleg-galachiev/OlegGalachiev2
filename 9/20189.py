f = open('20189')

k = 0
for i in f:
    a = sorted([int(x) for x in i.split()])
    num2 = [x for x in a if a.count(x) == 2]
    if len(num2) == 4:
        if a[0] * a[1] > sum(a[2:]):
            k += 1
print(k)