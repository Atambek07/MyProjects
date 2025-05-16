n = int(input("n="))
for num in range(2, n+1):
    s = 0
    d = 2
    while d < num:
        if num % d == 0:
            s += 1
        d += 1
    if s == 0:
        print(f'{num}', end=" ")
