a, b = map(int, input().split())
p = []
n = a
while n % 2023 != 0:
    n = n * 10 + a
    while n % 2023 != 0:
        n = n * 10 + b
if n % 2023 == 0:
    p.append(n)
print(str(p).split())

