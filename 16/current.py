import sys
sys.setrecursionlimit(10**6)

for x in range(1,1000):
    def f(n):
        if n>=3000:
            return n
        if n<3000:
            return n + x + f(n+2)

    if f(2984) - f(2988) == 5916:
        print(x)
