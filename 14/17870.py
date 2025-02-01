def per(x,y):
    c_0 = 0
    while x > 0:
        if x % y == 0:
            c_0 += 1
        x //= y
    return c_0



p = []
for x in range(1,2031):
    a = 7**170 +7**100 - x
    if per(a,7) == 71:
        p.append(x)
print(max(p))