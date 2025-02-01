for a in range(1,10000):
    flag = True
    for x in range(1,10000):
        f = ((x & 57 > 0) or (x & 99 > 0)) <= (x & a > 0)
        if f == 0:
            flag = False
            break
        if flag == True:
            print(a)