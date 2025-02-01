def num(a):
    b = set()
    for i in range(1, int(a**0.5)+1):
        if a % i == 0:
            b.add(i)
            b.add(a // i)
    return sorted(b)

for n in range(1_000_000,1_500_000):
    if len(num(n)) == 3:
        print(n, num(n)[-1])





