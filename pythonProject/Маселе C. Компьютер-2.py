a, b = map(int, input().split())
s = list(map(int, input().split()))
mx = max(s)
mn = min(s)
k = 2
p = 0
z = 0
s1 = 0
while p != 1:
    j = mx // k
    if j < mn:
        z += j
        p += 1
    else:
        k += 1
for i in s:
    s1 = s1 + (i // z)

print((z - b) * s1)
