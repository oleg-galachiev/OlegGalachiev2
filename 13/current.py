a = 2 * 216**8 + 4 * 36**12 + 6**15 - 1296
c = ''
while a >= 6:
    c += str(a%6)
    a //= 6
c += str(a)
c = c[::-1]
print(c)
