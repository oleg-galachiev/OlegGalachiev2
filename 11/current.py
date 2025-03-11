def f(x,y,z):
    if x == y:
        return 1
    if x > y:
        return 0
    if x < y:
        if z <= 2:
            return f(x-1,y,z+1) + f(x+5,y,z) + f(x*2,y,z)
        else:
            z = 0
            return f(x+5,y,z) + f(x*2,y,z)


print(f(5,34,0))
