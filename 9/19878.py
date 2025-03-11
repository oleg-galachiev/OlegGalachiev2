f = open('19878')

k = 0
for i in f:
    a = sorted([int(x) for x in i.split()])
    num3 = [x for x in a if a.count(x) == 3]
    num1 = [x for x in a if a.count(x) == 1]
    if len(num3) == 3 and len(num1) == 4 and sum(num1)/len(num1) <= num3[0]:
        k+=1
print(k)
