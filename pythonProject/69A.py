n = int(input())

s = [0, 0, 0]

for _ in range(n):
    f = list(map(int, input().split()))
    s[0] += f[0]
    s[1] += f[1]
    s[2] += f[2]

if s == [0, 0, 0]:
    print("YES")
else:
    print("NO")




