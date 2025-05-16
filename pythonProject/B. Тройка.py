def gg(j):
    o=0
    p=0
    for i in a:
        if j == i:
            o += 1
    if o >= 3:
        return 3
    else:
        return 1


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = 0
    p = 0
    for i in a:
        s = gg(i)
        if s == 3:
            m = i
        else:
            p += 1
    if p >= n:
        print(-1)
    else:
        print(m)
