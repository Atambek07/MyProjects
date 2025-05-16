word = input()
count_up = 0
count_down = 0
for i in word:
  if i.isupper():
    count_up += 1
  else:
    count_down += 1
if count_up > count_down:
  print(word.upper())
else:
  print(word.lower())