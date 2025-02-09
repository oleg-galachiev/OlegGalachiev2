from string import ascii_lowercase
a = '0123456789' + ascii_lowercase
for p in range(8,36):
    for x in a[:p]:
        for y in a[:p]:
            if int('1' + x + '77', p) + int(x + x + '77',p) == int(y + '0' + y + y,p):
                print(int(y + x + y + x, p))