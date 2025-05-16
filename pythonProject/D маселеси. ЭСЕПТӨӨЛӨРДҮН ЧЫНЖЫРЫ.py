s = 1
k = []
for _ in range(int(input())):
    a, b = input().split()
    k.append(b)
    b = int(b)
    if a == "A":
        s += b
    if a == "S":
        s -= b
    if a == "M":
        s *= b
    if a == "R":
        s *= (int(k[-2]) ** int(k[-1]))
    print(s)
