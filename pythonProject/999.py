def S(n):
    return sum(map(int, str(n)))


def Aa(a, b):
    c = 0

    for x in range(1, a + 1):
        for y in range(1, b + 1):
            if S(x + y) ==S(x) + S(y):
                c += 1

    return c

a, b = map(int, input().split())

print(Aa(a,b))
