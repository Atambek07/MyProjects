def find_remainder(M, N, K):
    result = (pow(M, N, 2) * (pow(M, 2) + 23)) % K
    return result

# Считываем входные данные
input_data = input().split()
M, N, K = map(int, input_data)

# Находим остаток и выводим результат
result = find_remainder(M, N, K)
print(result)
