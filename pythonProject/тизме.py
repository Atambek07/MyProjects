#2 ТИЗМЕ БЕРИЛГЕН.бирнчи тизмене окуучулардын фамилия,экинчи тизмеде баалары.
#5 алган окуучуларды фамилясын чагар
f1 = []
f = list(input().split())
b = list(map(int,input().split()))
a = len(f)
for i in range(a):
    if b[i] == 5:
        f1.append(f[i])
        print(f1)