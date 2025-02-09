m = 278
for n in range(1,1000):
    d = m | n
    c = bin(d)[2:]
    if c.count('1') == 7:
        print(n)
        break