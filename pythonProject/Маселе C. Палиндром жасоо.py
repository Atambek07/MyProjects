def min_letters_to_palindrome(s):
    count = 0
    length = len(s)

    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            count += 1

    return count

# Ввод данных
s = input()

# Подсчет и вывод результата
result = min_letters_to_palindrome(s)
print(result)
