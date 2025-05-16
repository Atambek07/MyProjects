from math import sin , sqrt , e
x = float(input("x="))
p = float(input("p="))
a = e ** sqrt(abs(x))
b = (sin(p**2) + x ** 3)
y = (a ** 3)/(b ** 2)
print(y)