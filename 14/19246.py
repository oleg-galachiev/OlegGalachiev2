from string import ascii_lowercase
p = []
for x in '0123456789' + ascii_lowercase[:15]:
    num1 = int('11353' + x + '12', 25)
    num2 = int('135' + x + '21', 25)
    summ = num2 + num1
    if summ % 24 == 0:
        p.append(summ//24)
print(max(p))

