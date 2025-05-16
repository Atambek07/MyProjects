def Aa(n, m):
    c2 = 0
    c5 = 0
    for i in m:
        while i % 2 == 0:
            c2 += 1
            i //= 2
        while i % 5 == 0:
            c5 += 1
            i //= 5
    return min(c2, c5)

n = int(input())
a = list(map(int, input().split()))
s = Aa(n, a)
print(s)