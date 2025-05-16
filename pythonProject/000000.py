a = input()
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
c = []
for i in range(9):
    if a[0] + str(i) not in c:
        c.append(a[0] + str(i))
c.remove(a)
for h in s:
    c.append(h + a[1])
c.remove(a)
for j in c:
    print(j)
