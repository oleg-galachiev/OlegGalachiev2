import sys
sys.setrecursionlimit(10**6)

def f(n):
    if n < 3:
        return 3
    else:
        c = 2 * n + 5 + f(n-2)
        return c

print(f(3027)-f(3023))