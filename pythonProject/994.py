def Aa(n):
    s = 0
    m = (n // 2) * 2 - 1

    for i in range(1, m + 1, 2):
        c = 0
        for j in range(i, m + 1, 2):
            c += j
            if c == n:
                s += 1
                break
    return s

n = int(input())
print(Aa(n))