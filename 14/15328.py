from string import ascii_lowercase
for x in '0123456789' + ascii_lowercase[:17]:
    summ = int('123' + x + '24', 27) + int('135' + x + '78', 27)
    if summ % 26 == 0:
        print((summ//26))