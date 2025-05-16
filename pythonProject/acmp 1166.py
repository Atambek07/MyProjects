input()
a = list(map(int, input().split()))
n = []
m = []
s1 = 1
for i in a:
    if int(i) % 2 == 0:
        s = 0
        for j in str(i):
            s += int(j)
        n.append(s)
    else:
        s1 = 1
        for j1 in str(i):
            s1 *= int(j1)
        m.append(s1)
print(max(n), max(m))
