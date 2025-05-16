s = input()
a = int(s[0])
b = int(s[2])
c = int(s[-1])
if a + b != c and a == b:
    b1 = c - a
    print(a, "+", b1, "=", c, sep="")
    a1 = c - b
    print(a1, "+", b, "=", c, sep="")
elif a + b != c and a != b:
    b1 = c - a
    print(a, "+", b1, "=", c, sep="")
    a1 = c - b
    print(a1, "+", b, "=", c, sep="")
    c1 = a + b
    print(a, "+", b, "=", c1, sep="")
else:
    print(s)
