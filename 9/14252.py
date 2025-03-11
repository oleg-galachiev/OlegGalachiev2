f = open('14252')


k = 0
for i in f:
    a = [int(x) for x in i.split()]
    num4 = [x for x in a if a.count(x) == 4]
    num1 = [x for x in a if a.count(x) == 1]
    if len(num4) == 4 and len(num1) == 3 and (num1[0]+num1[1]+num1[2])/3 < sum(a)/7:
        k+=1
print(k)
