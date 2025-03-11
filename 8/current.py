from itertools import product

k = 0
ar = product('0123456', repeat = 5)
for i in ar:
    a = ''.join(i)
    if a.count('6') == 1 and a[0] != '0':
        chet = 0
        nechet = 0
        for n in a:
            if int(n) % 2 == 0:
                chet += int(n)
            else:
                nechet+= int(n)
        if chet<nechet:
            k+=1
print(k)
