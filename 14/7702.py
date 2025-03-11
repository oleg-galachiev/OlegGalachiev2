from string import ascii_lowercase
p = []
for x in range(0,18):
    for y in range(9,18):
        if int(x) < int(y):
            num1 = 5 * 18**3 + x * 18**2 + y * 18**1 + 10 * 18**0
            num2 = 1 * y**3 + 8* y**2 + x * y**1 + 7 * y**0
            p.append(num1 + num2)
print(len(set(p)))
