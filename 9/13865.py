f = open('13865')

k = 1
for i in f:
    a = sorted([int(x) for x in i.split()])
    num1 = [x for x in a if a.count(x) == 1]
    if int(len(num1) == 7) + int(2*(a[0]+a[6]) <= 3*(sum(a[1:6]))) == 1ф:
        k+=1
print(k)
