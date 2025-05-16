n = input()
a1 = []
for j in n:
    a1.append(j)
a2 = []
c1 = []
s = 120
for i in range(6,70):
    s *= i
    a2.append(s)
    c1.append(len(str(s)))
a3 = len(a1)
d = c1.index(a3)
print(a2[d])
print(a2)