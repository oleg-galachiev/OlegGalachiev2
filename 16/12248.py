import sys
sys.setrecursionlimit(10**6)


def f(n):
    if n <= 3:
        return 1
    else:
        return (n + 3) * f(n - 2)



c = f(2028)/f(2024)
print(c)