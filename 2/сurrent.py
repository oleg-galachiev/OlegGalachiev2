for x in range(0,2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                f = (not(((not x) or y) and (not w))) or (not (z and (not(y and w))))
                if f == 0:
                    print(x,y,z,w)