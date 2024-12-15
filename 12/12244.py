c = 0
for n in range(3,10001):
    a = '3' + '5' * n
    while '333' in a or '555' in a:
        if '555' in a :
            a = a.replace('555', '3', 1)
        else:
            a = a.replace('333', '5', 1)
    print(a)


