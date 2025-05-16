from math import sqrt
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
d = b ** 2 - 4 * a * c

if a == 0:
    print("Error")

elif d > 0:
    x1 = (-(b) + sqrt(d))/(2 * a)
    x2 = (-(b) - sqrt(d))/(2 * a)
    print(f'x1={x1}')
    print(f'x2={x2}')

elif d == 0:
    x = -(b)/(2*a)
    print(f'x={x}')

else:
    print("Error")
