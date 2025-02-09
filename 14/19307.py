def count(x):
    c = 0
    while x > 0:
        if x % 5 == 0:
            c += 1
        x //= 5
    return c


print(count(15625**16 - 3125**3 * 25**19 + 625**4 - 2005))