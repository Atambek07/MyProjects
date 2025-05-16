x = int(input("Сколько лет Танье: "))
y = int(input("Сколько лет Митье: "))


z = (x + y) // 2
print("Middle old:", z)


if z > x:
    print(z - x, "year difference have Tanya")
elif x > z:
    print(x - z, "year difference have Tanya")
else:
    print("0 year difference have Tanya")


if z > y:
    print(z - y, "year difference have Mitya")
elif y > z:
    print(y - z, "year difference have Mitya")
else:
    print("0 year difference have Mitya")
