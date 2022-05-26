import sys


if __name__ == '__main__':
    width, height = map(int, sys.stdin.readline().split())
    tomato_box = []
    tomatoes = []
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    day = -1

    for _ in range(height):
        tomato_box.append(list(map(int, sys.stdin.readline().split())))

    for y, tomato_vector in enumerate(tomato_box):
        for x, is_tomato in enumerate(tomato_vector):
            if is_tomato == 1:
                tomatoes.append((y, x))

    # bfs
    while tomatoes:
        temp_tomatoes = tomatoes[:]
        tomatoes.clear()
        for tomato in temp_tomatoes:
            for direction in directions:
                next_y = direction[0] + tomato[0]
                next_x = direction[1] + tomato[1]
                if 0 <= next_y < height and 0 <= next_x < width:
                    if tomato_box[next_y][next_x] == 0:
                        tomato_box[next_y][next_x] = 1
                        tomatoes.append((next_y, next_x))

        day += 1

    for y, tomato_vector in enumerate(tomato_box):
        for x, is_tomato in enumerate(tomato_vector):
            if not is_tomato:
                day = -1
    print(day)
