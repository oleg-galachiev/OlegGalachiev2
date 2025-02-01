f = open("17_18176.txt")
a = [int(x) for x in f]

mn = []
for i in a:
    if i > 0 and str(i)[-1] == "4":
        mn.append(i)
mn = min(mn)
p = []
for l in range(len(a) - 2):
    k = [a[l], a[l+1], a[l+2]]
    all_digits = str(abs(k[0])) + str(abs(k[1])) + str(abs(k[2]))
    sm = sum(map(int, list(all_digits)))
    if sm == mn:
        p.append(sum(k))

print(len(p), max(p))

