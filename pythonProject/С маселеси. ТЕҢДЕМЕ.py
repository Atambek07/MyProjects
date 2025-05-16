k, m, n = map(int, input().split())
for i in range(1, n):
    if (i ** k) + m * i == n:
        print(i)
        break
    else:
        print(0)
        break
