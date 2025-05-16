def kth_sum_element(n, m, k, A, B):
    sums = []

    # Создаем массив сумм пар
    for i in range(n):
        for j in range(m):
            sums.append(A[i] + B[j])

    # Сортируем массив сумм пар
    sorted_sums = sorted(sums)

    # Возвращаем k-й элемент
    return sorted_sums[k - 1]


# Ввод данных
n, m, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Подсчет и вывод результата
result = kth_sum_element(n, m, k, A, B)
print(result)
