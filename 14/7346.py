for x in range(67):
    num1 = 3 * 81**3 + x * 81**2 + 2 * 81 + 1
    num2 = 1 * 67**3 + 7 * 67**2 + x * 67 + 4
    summ = num1 + num2
    if summ % 35 == 0:
        print(summ//35)