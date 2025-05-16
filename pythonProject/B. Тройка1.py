
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    k = 0
    p = 0
    m=[]
    for i in a:
        if i not in m:
            m.append(i)
    for j in m:
        s = a.count(j)
        if s >= 3:
            k = j
        else:
            p += 1
    if p >= n:
        print(-1)
    else:
        print(k)
