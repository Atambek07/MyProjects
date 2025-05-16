def Aa(a, b, c):
    da = set()
    db = set()

    for i in range(1, a + 1):
        if a % i == 0:
            da.add(i)

    for i in range(1, b + 1):
        if b % i == 0:
            db.add(i)

    cd = da.intersection(db)
    if len(cd) < c:
        return 0

    return sorted(cd)[c - 1]

a, b, c = map(int, input().split())
print(Aa(a, b, c))
