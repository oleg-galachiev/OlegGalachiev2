def coun(x):
    c = 0
    while x > 0:
        if x % 25 == 0:
            c += 1
        x //= 25
    return c



print(coun(3 * 3125**9 + 2 * 625**8 - 4 * 625**7 + 3 * 125**6 - 2 * 25**5 - 2024))