def per(x,y):
    c_4 = 0
    while x > 0:
        if x % y == 4:
            c_4 += 1
        x //= y
    return c_4



p = []
for x in range(1,5556):
    a = 5**150 + 5**135 - x
    if per(a,5) == 134:
        p.append(x)
print(max(p))
