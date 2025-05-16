a,b = map(int,input().split())
a1 = []
b1 = []
while a * b != a:
    a += a
    a1.append(a)
    b += b
    b1.append(b)
for i in a1:
    for j in b1:
        if i == j:
            print(j)