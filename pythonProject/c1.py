x = int (input())
while True:
    s = str(x);
    if s.count('1') == 1 and s.count('0') == 1 and s.count('2') == 2:
        print(s)
        break;
    x += 1