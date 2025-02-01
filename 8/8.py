import itertools


p = []
f = 0
sim = '0123456789abcde'
ar = itertools.product(sim, repeat=8)
for i in ar:
    p.append(list(i))
for k in p:
    if p.count('0') == 2 and p.count('a') + p.count('b') + p.count('c') + p.count('d') + p.count('e') <= 4:
        f += 1
print(f)
