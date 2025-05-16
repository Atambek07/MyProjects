n = int(input())
k = len(str(n))
s = 0
for i in range(1, n+1, 2):
    s += 1
a = n // (10 ** (k - 1))
b = a - 2
c = s - (b * 5)
print(c)
print(s)