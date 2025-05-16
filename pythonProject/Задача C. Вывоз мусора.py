k = int(input())
m = int(input())
exits = list(map(int, input().split()))
n = int(input())
trash_bags = list(map(int, input().split()))

total_distance = 0

for bag in trash_bags:
    nearest_exit = min(exits, key=lambda x: abs(x - bag))
    distance_to_exit = abs(nearest_exit) + 1  # Расстояние до выезда (1 по выезду)

    if k >= n:
        total_distance += distance_to_exit
        break
    else:
        total_distance += distance_to_exit
        n -= k

print(total_distance)
