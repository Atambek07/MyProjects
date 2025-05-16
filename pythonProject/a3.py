n = list(map(int, input().split()))
s = 1
s1 = 0
for i in n:
    if i < 0:
        s *= i
    if i > 0:
        s1 += i
print(s)
print(s1)
if s > s1:
    print("Терс сандардын кобойтундусу чон")
elif s1 > s:
    print("Он сандардын суммасы чон")
else:
    print("Экоо барабар")