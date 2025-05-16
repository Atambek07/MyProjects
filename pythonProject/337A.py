n, n1 = map(int, input().split())
f = list(map(int, input().split()))

f.sort()

m = float("inf")

for i in range(n1 - n + 1):
    m = min(m, f[i + n - 1] - f[i])

print(m)
