def per(x):
    c = ''
    while x > 0:
        c += str(x%3)
        x //= 3
    return c[::-1]



p = []
for n in range(1,1000):
    c = per(n)
    if n % 3 == 0:
        c += c[-2:]
    else:
        summ = 0
        for i in c:
            summ += int(i)
        c += per(summ)
    r = int(c, 3)
    if r > 220:
        if r % 2 == 0:
            print(r)
            break

