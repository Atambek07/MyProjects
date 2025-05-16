import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def kth_common_divisor(a, b, k):
    common_divisor = gcd(a, b)

    divisors = []
    sqrt_divisor = int(math.sqrt(common_divisor))
    for i in range(1, sqrt_divisor + 1):
        if common_divisor % i == 0:
            divisors.append(i)
            if i != common_divisor // i:
                divisors.append(common_divisor // i)

    divisors.sort()

    if len(divisors) < k:
        return 0

    return divisors[k - 1]

a, b, k = map(int, input().split())
print(kth_common_divisor(a, b, k))