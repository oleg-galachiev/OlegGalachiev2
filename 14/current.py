p = []
for x in '0123456789a':
    num1 = int('3364' + x, 11)
    num2 = int(x + '7946', 12)
    summ = int('55' + x + '87', 14)
    if num2 + num1 == summ:
        p.append([x, summ])
print(min(p))

