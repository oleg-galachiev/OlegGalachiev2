def per(x,y):
    c_b = 0
    c_c = 0
    while x > 0:
        if x % y == 11:
            c_b += 1
        if x % y == 12:
            c_c += 1
        x //= y
    return abs(c_b - c_c)


a = 283**382 + 9**15 + 2**3
print(per(a, 14))