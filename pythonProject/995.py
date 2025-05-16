def Aa(a,b):
    s = []
    for i in range(a,b+1):
        p = []
        for j in range(1,i+1):
            if i % j == 0 and j % 2 == 1:
                p.append(j)
        s.append(max(p))
    return sum(s)

a, b = map(int,input().split())
print(Aa(a,b))
