# Функция для вычисления расстояния между двумя точками на сетке
def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# Считывание данных
cat1_x = int(input())
cat1_y = int(input())
cat2_x = int(input())
cat2_y = int(input())
cat3_x = int(input())
cat3_y = int(input())
cat4_x = int(input())
cat4_y = int(input())

# Вычисление расстояний от четырех котов до трех валунов
distances = [
    (distance(cat1_x, cat1_y, cat2_x, cat2_y), 1),
    (distance(cat2_x, cat2_y, cat3_x, cat3_y), 2),
    (distance(cat3_x, cat3_y, cat1_x, cat1_y), 3),
    (distance(cat4_x, cat4_y, cat1_x, cat1_y), 1),
    (distance(cat4_x, cat4_y, cat2_x, cat2_y), 2),
    (distance(cat4_x, cat4_y, cat3_x, cat3_y), 3),
]

# Сортировка расстояний по возрастанию
distances.sort()

# Нахождение номера валуна, к которому четвертый кот может добраться быстрее всех
fastest_valun = distances[0][1]

# Вывод результата
print(1)
print(fastest_valun)
