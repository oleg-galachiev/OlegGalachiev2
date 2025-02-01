def per(x,y):
    c = ''
    while x >= y:
        c += str(x % y)
        x //= y
    c += str(x)
    return c[::-1]


num = 7**21 + 49**13 - 7**10
c = per(num,7)
print(c.count('6'))