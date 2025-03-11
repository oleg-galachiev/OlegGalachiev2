f = open('19241')
k = 0
for i in f:
    k+=1
    a = [x for x in i.split()]
    num3 = [x for x in a if a.count(x) == 3]
    num1 = [x for x in a if a.count(x) == 1]
    if len(num3) == 6 and len(num1) == 1 and int(sum(num3)/len(num3)) < int(num1[0]):
        print(k)
