f = open('12797')


k = 0
for i in f:
    a = sorted([int(x) for x in i.split()])
    num2 = [x for x in a if a.count(x) == 2 and x % 2 == 0]
    num1 = [x for x in a if a.count(x) == 1 and x % 2 != 0]
    if len(num2) == 2 and len(num1) == 2:
        k+=1
print(k)