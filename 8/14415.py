from itertools import *

count = 0
ar = product('0123456789ab', repeat = 5)
for i in ar:
    a = ''.join(i)
    if a[0] != "0":
        a = a.replace('0', '-')
        a = a.replace('2', '-')
        a = a.replace('4', '-')
        a = a.replace('6', '-')
        a = a.replace('8', '-')
        a = a.replace('a', '+')
        if a.count('+') == 2 and not '-7' in a and not '7-' in a and not '+7' in a and not '7+' in a:
            count += 1
print(count)
