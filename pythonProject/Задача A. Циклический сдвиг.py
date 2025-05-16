a = input()
s = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"
     , "s","t","u","v","w","x","y","z"]

a1 = s.index(a[0])
a2 = s.index(a[1])
a3 = s.index(a[2])
if a3 - a2 == a2 - a1:
     print("YES")
else:
     print("NO")