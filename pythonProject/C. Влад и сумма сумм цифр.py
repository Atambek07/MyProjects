for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(1,n+1):
        a.append(sum(map(int, str(i))))
    print(sum(a))
