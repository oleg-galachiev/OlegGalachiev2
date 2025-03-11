f = open('8467')

k = 0
for i in f:
    a = sorted([int(x) for x in i.split()])
    num1 = [x for x in a if a.count(x) == 1]
    l = int(len(num1)==5) + int(2*(a[0]+a[4])<sum(a[1:4]))
    if l == 1:
        k+=1
print(k)