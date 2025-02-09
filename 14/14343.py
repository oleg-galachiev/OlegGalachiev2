def coun(x):
    c = 0
    while x > 0:
        c += x % 7
        x //= 7
    return c


print(coun(5 * 343**2031 + 4 * 49**2142 -3 * 7**111 + 7**222))