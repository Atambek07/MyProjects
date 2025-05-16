def atam(n):
    s = []
    k = []
    while n != 0:
        a = n % 10
        n = n // 10
        s.append(a)
    s1 = sum(s)
    if s1 < 10:
        return s1
    else:
        while s1 != 0:
            a1 = s1 % 10
            s1 = s1 // 10
            k.append(a1)
        s2 = sum(k)
        if s2 < 10:
            return s2

n = int(input())
print(atam(n))
