from math import sqrt
for x in range(39):
    for y in range(39):
        num = 5 * 39**8 + 8 * 39**7 + x * 39**6 + 7 * 39**5 + 2 * 39**4 + 3 * 39**3 + y * 39**2 + 4 * 39 + 9
        if num % 38 == 0:
            if sqrt(x * 39 + y) % 1 == 0:
                print(x * 39 + y)