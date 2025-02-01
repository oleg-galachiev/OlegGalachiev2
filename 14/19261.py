from string import ascii_lowercase


p = []
for x in '0123456789' + ascii_lowercase[:28]:
    num1 = int('98' + x + '31', 37)
    num2 = int('1' + x + '924', 37)
    summ = num1 + num2
    if summ % 21 == 0:
        p.append(summ // 21)
print(max(p))
