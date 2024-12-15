c = 0
for a in range(1, 1000000):
    flag = True
    for x in range(a, 10000):
        f = (x & a == 0) or not(x & 37 == 0) or not(x & 12 == 0)
        if f == False:
            flag = False
            break
        if flag == True:
           c += 1
print((a))