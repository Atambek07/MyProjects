from math import sqrt , log
x = float(input("x="))
t = float(input("t="))
a = log(x)
b = sqrt((x ** 2)+ (t ** 2))
y = abs(a - b * x) * (1./5)
print(y)