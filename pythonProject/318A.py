n, k = map(int, input().split())

if k <= (n + 1) // 2:
    s = 2 * k - 1
else:
    s = 2 * (k - (n + 1) // 2)

print(s)
