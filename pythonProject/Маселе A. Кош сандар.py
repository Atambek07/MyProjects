
def Aa(a,b):
    k = 0
    for i in range(a, b+1):
        s = len(str(i))
        s1 = s // 2
        if i % (10 ** s1) == i // (10 ** s1):
            k += 1
    return k

a,b = map(int, input().split())
print(Aa(a,b))