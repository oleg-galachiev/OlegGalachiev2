from itertools import product, repeat

ar = product('айлм', repeat = 5)

k = 0
for i in ar:
    k+=1
    a = ''.join(i)
    if not 'м' in a and not 'л' in a and not 'йй' in a:
        print(k)