p = []
for x in range(100,191):
    for y in range(100,10000):
        d = str(int(str(x)[2]) + int(str(y)[2])) + str(int(str(x)[0]) + int(str(y)[0])) + str(int(str(x)[1]) + int(str(y)[1]))
        c = d[-4:-1]
        if c == '002':
            print(x, c)