n = int(input("n="))
m = int(input("m="))
x = [[0] * m for k in range(n)]
for i in range(n):
    for j in range(m):
        x[i][j] = int(input())

for i in range(n):
    s = 0
    for j in range(m):
        if x[i][j] < 0:
            s += 1
    print(s)
