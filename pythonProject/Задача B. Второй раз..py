a = int(input())
s = input().split()
for i in range(a):
    k = s.count(s[i])
    if k == 1:
        print(s[i])