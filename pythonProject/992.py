a, b, c, d = map(int, input().split())
l1 = a * b
l2 = c * d
l3 = a * c
l4 = b * d
l5 = a * d
l6 = b * c
s1 = l1 + l2
s2 = l3 + l4
s3 = l5 + l6
print(max(s1, s2, s3))