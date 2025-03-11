from fnmatch import fnmatch

for i in range(3123,10**9+1,3123):
    if fnmatch(str(i),'12*63?5?'):
        print(i)