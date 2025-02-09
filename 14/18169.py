def count(x):
    c = 0
    while x > 0:
        if x % 3 == 2:
            c += 1
        x //= 3
    return c



for x in range(1,100000):
    if count(3**2000 + 3**10 - x) == 2000:
        print(x)
