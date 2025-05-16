a,b = input().split()
s =["0","BIR","EKI","UECH","TOERT","BESH","ALTY","JETI","SEGIZ","TOGUZ","ON"]
a = int(a)
k=[]
if int(a)==1:
    for i in range(0,len(b)):
        l=b[:i]+b[i+1:]
        for j in s:
            if l==j:
                k.append(s.index(j))
            else:
                k.append(0)

    print(int(max(k)))
elif int(a)==2:
    for i in range(0,len(b)):
        for t in range(i,len(b)):
            l=b[:i]+b[i+1:]
            p=l[:t]+l[t+1:]
            for j in s:
                if p==j:
                    k.append(s.index(j))
                else:
                    k.append(0)
    print(int(max(k)))
elif int(a)==3:
    for i in range(0,len(b)):
        for t in range(i,len(b)):
            for e in range(t,len(b)):
                l=b[:i]+b[i+1:]
                p=l[:t]+l[t+1:]
                p1=p[:e]+p[e+1:]
                for j in s:
                    if p1==j:
                        k.append(s.index(j))
                    else:
                        k.append(0)
    print(int(max(k)))
