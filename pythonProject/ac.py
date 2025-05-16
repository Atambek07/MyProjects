def check(i):
    c = 0
    for j in str(i):
        if int(j) % 2 == 1:
            c += 1
    return c


s = 0
n = int(input())
for i in range(1, n + 1):
    k = len(str(i))
    if i % 2 != 0 and i // (10 ** (k - 1)) % 2 != 0:
        d = check(i)
        if d == k:
            s += 1
print(s)
