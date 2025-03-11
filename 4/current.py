def per(x):
    c = ''
    while x > 0:
        c += str(x%4)
        x //= 4
    return c[::-1]



for i in range(1000):
    c = per(i)
    c = c.zfill(5)
    c = c.replace('0','а')
    c = c.replace('1', 'й')
    c = c.replace('2', 'л')
    c = c.replace('3', 'м')
    if not 'м' in c and not 'л' in c and not 'йй' in c:
        print(i+1,c)
