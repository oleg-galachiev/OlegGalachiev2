from string import ascii_uppercase


a = '0123456789' + ascii_uppercase
p = []
for y in range(9, 18):
    for x in range(y):
        num1 = int('5' + a[x] + a[y] + 'a', 18)
        num2 = int('18' + a[x] + '7', int(y))
        r = num1 + num2
        p.append(r)
c = []
for i in p:
    if not i in c:
        c.append(i)
print(len(c))