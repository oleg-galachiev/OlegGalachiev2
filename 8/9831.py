from itertools import *

count = 0
ar = product('0123456789abcdef', repeat = 3)
for i in ar:
    a = ''.join(i)
    if len(set(a)) == len(a) and a[0] != '0' :
        a = a.replace('0', '-')
        a = a.replace('2', '-')
        a = a.replace('4', '-')
        a = a.replace('6', '-')
        a = a.replace('8', '-')
        a = a.replace('a', '-')
        a = a.replace('c', '-')
        a = a.replace('e', '-')
        a = a.replace('1', '+')
        a = a.replace('3', '+')
        a = a.replace('5', '+')
        a = a.replace('7', '+')
        a = a.replace('9', '+')
        a = a.replace('b', '+')
        a = a.replace('d', '+')
        a = a.replace('f', '+')
        if not '--' in a and not '++' in a:
            count+=1
print(count)



