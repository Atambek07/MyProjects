n = int(input())
s = 0
k = 0
d = 0
for _ in range(n):
    a, b = map(int, input().split())
    k += b
    if a == 1:
        s += 20
        d += 1
print(s-(k+d))
