import itertools



sim = '012345678'
arl = itertools.product(sim, repeat=5)
p =[]
for i in arl:
    p.append(list(i))

