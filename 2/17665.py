for x in range(0,2):
    for w in range(0,2):
        for z in range(0,2):
            for y in range(0,2):
                f = (not z or not(not(y) or x)) or w
                if not f:
                    print(x,y,w,z)