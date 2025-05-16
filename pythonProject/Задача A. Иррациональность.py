import math

def find_points(D):
    points = []
    K = 0
    for x in range(0, 2*D+1):
        for y in range(x, 2*D+1):
            distance = math.sqrt(x**2 + y**2)
            if math.isclose(distance, D*math.sqrt(2)):
                points.append((x, y))
                K += 1

    return points, K

D = int(input().strip())

points, K = find_points(D)

print(K)
for point in points:
    print(point[0], point[1])