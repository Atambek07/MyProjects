def binary(x):
    e = ""
    while x != 0:
        k = x % 2
        x //= 2
        e = str(k)+e
    return e


n = int(input())
while n != 0:
    print(binary(n))
    n = int(input())
