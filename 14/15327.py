def count(x):
    c = 0
    while x > 0:
        if x % 27 > 9:
            c += 1
        x //= 27
    return c


print(count(3 * 2187**2020 + 3 * 729**2021 - 2 * 81**2022 + 27**2023 - 4 * 3**2024 - 2029))