s = input()
s1 = "CHYCHKAN"
k = 0
if len(s) == len(s1):
    for i in s:
        for j in s1:
            if j == i:
                k += 1
print(len(s)-k)