from string import ascii_lowercase
p = []
for y in '9' + ascii_lowercase[:8]:
    for x in '0123456789' + ascii_lowercase[:8]:
        p.append(int('5' + x + y +'a',18)+int('1' + '8' + x + '7', int(y)))