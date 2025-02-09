def per(x):
    c = ''
    while x > 0:
        c += str(x%4)
        x //= 4
    return c[::-1]

p = []
for n in range(1,1000):
    b = per(n)
    if n % 4 == 0:
        b = '2' + b + '03'
    else:
        b += per(n % 4 * 5)
    r = int(b, 4)
    if r < 567:
        p.append(n)
print(max(p))
