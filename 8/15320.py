from itertools import product,repeat


ar = product('апрсу', repeat = 5)
k = 0
for i in ar:
    k+=1
    a = ''.join(i)
    if a.count('у') <= 1 and not 'аа' in a:
        print(k)
        break
