import sys


if __name__ == '__main__':
    width, height, depth = map(int, sys.stdin.readline().split())
    tomato_box = []
    tomatoes = []
    directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)] # z, y, x
    day = -1

    for i in range(depth):
        tomato_box.append([])
        for _ in range(height):
            tomato_box[i].append(list(map(int, sys.stdin.readline().split())))

    for z, tomato_plane in enumerate(tomato_box):
        for y, tomato_vector in enumerate(tomato_plane):
            for x, is_tomato in enumerate(tomato_vector):
                if is_tomato == 1:
                    tomatoes.append((z, y, x))

    # bfs
    while tomatoes:
        temp_tomatoes = tomatoes[:]
        tomatoes.clear()
        for tomato in temp_tomatoes:
            for direction in directions:
                next_z = direction[0] + tomato[0]
                next_y = direction[1] + tomato[1]
                next_x = direction[2] + tomato[2]
                if 0 <= next_z < depth and 0 <= next_y < height and 0 <= next_x < width:
                    if tomato_box[next_z][next_y][next_x] == 0:
                        tomato_box[next_z][next_y][next_x] = 1
                        tomatoes.append((next_z, next_y, next_x))

        day += 1

    for z, tomato_plane in enumerate(tomato_box):
        for y, tomato_vector in enumerate(tomato_plane):
            for x, is_tomato in enumerate(tomato_vector):
                if not is_tomato:
                    day = -1
    print(day)
