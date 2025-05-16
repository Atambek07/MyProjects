m = int(input())
l = [0]*m
s = 0
for i in range(m):
    a = list(map(int, input().split()))
    l.append(a)
for j in range(m):
    s += l[0][j]
    s += l[j][0]
    s += l[m][j]
    s += l[j][m]
print(s)
