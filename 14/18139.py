def per(x,y):
    c = 0
    while x > 0:
        if x % y == 0:
            c += 1
        x //= y
    return c
a = 216**1315 - 4*36**1502 + 5*36**1510 - 3*6**1331 - 253
print(per(a, 6))