def convert_absolute_to_relative(absolute_route):
    directions = {'N': {'S': 'N', 'W': 'W', 'E': 'E'},
                  'S': {'N': 'S', 'W': 'E', 'E': 'W'},
                  'W': {'N': 'W', 'S': 'N', 'E': 'S'},
                  'E': {'N': 'E', 'S': 'W', 'W': 'N'}}

    current_direction = 'N'
    relative_route = []

    for command in absolute_route:
        if command in directions[current_direction]:
            current_direction = directions[current_direction][command]
            relative_route.append(current_direction)

    return ''.join(relative_route)


# Example route
absolute_route = input().strip()
relative_route = convert_absolute_to_relative(absolute_route)
print(relative_route)