def per(x,y):
    alph = 'abcde'
    c = ''
    while x > 0:
        if x % y > 9:
            c = alph[x%y-10] + c
        else:
            c = str(x%y) + c
        x //= y
    return c




p = []
num = 11 * 15**65 + 18 * 15**38 - 14 * 15**17 + 19 * 15**11 + 18338
c = per(num, 15)
c = list(c)
print(len(set(c)))



