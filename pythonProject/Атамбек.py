n = int(input())
for i in range(n):
    s = input()
    a = s.find("a")
    b = s.find("b")
    c = s.find("c")
    if a == 0 and b == 1 and c == 2:
        print("Yes")
    elif a == 0 and b == 2 and c == 1:
        print("Yes")
    elif a == 2 and b == 1 and c == 0:
        print("Yes")
    elif a == 1 and b == 0 and c == 2:
        print("Yes")
    else:
        print("No")