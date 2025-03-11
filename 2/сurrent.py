a = 113874

def f(n):
    divs = set()
    for i in range(1,int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n//i)
    return sorted(divs)


print(f(a))
