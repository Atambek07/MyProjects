n = int(input())
s = 1
s1 = 1
if n % 2 == 0:
    for i in range(2,n+1,2):
        s1*=i
else:
    for j in range(1,n+1,2):
        s1 *= j
print(s1)
