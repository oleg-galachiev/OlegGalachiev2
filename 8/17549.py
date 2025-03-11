from itertools import *

ar = product('косуф', repeat = 5)

k = 0
for i in ar:
    k+= 1
    a = ''.join(i)
    if not 'ф' in a and a.count('у') == 2:
        print(k)
