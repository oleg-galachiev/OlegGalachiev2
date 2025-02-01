import sys
sys.setrecursionlimit(10**6)

def f(n):
    if n < 7:
        c = 7
    else:
        c = 2*n + f(n-1)
    return c



c = f(2024) - f(2022)
print(c)