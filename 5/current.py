k = 0
for n in range(300,401):
    b = sorted(list(str(n)))
    if b[0] != '0' and b[1] != '0':
        mn = b[0] + b[1]
        mx = b[2] + b[1]
    if b[0] == '0' and b[1] != '0':
        mn = b[1] + b[0]
        mx = b[2] + b[1]
    if b[0] == '0' and b[1] == '0':
        mn = b[2] + b[1]
        mx = b[2] + b[1]
    r = int(mx) - int(mn)
    if r == 20:
        k+=1
print(k)










    # b = bin(n)[2:]
    # s1 = 0
    # s2 = 0
    # for i, v in enumerate(b):
    #     if int(i) % 2 != 0 and int(v) == 1:
    #         s1 += 1
    # for b, c in enumerate(b):
    #     if int(b) % 2 == 0 and int(c) == 0:
    #         s2+= 1
    # r = abs(s2 - s1)
    # if r == 5:
    #     print(n)
    #     break




