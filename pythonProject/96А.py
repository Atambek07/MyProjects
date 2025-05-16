def Aa(n):
    c = 0
    c1 = 0

    for i in n:
        if i == '0':
            c += 1
            c1 = 0
        elif i == '1':
            c += 1
            c1 = 0

        if c >= 7 or c1 >= 7:
            return "YES"

    return "NO"

n = input()

print(Aa(n))
