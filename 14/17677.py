def per(x):
    c = 0
    while x > 0:
        if x % 6 == 0:
            c+=1
        x //= 6
    return c


for x in range(1,2031):
    c = per(6**260 + 6**160 + 6**60 - x)
    if c == 202:
        print(x)