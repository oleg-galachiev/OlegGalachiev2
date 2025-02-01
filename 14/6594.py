for x in '0123456789abc':
    num1 = int('753' + x + '2', 13)
    num2 = int('2' + x + '173', 13)
    sum = num1 + num2
    if sum % 12 == 0:
        print(sum // 12)
        break