def poz(n,m):
    if (n-m)>0:
        return True
    else:
        return False
p =[]
for a in range(0,1000):
    flag = True
    for x in range(0,500):
        for y in range(0,500):
            f = not(poz(x+y,73)) or not(poz(37,x-y)) or poz(y,a)
            if not f:
                flag = False
                break
        if not flag:
            break
    if flag:
        p.append(a)
print(max(p))