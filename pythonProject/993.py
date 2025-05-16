n = int(input())
ans = n
for i in range(2, n):
    for j in range(i, n):
        if (i * j <= n):
            ans += 1
        if i * j > n: break;

print(ans)