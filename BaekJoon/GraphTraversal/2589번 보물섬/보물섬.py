import sys
from collections import deque

if __name__ == '__main__':
    height, width = map(int, sys.stdin.readline().split())
    treasure_map = []
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for _ in range(height):
        treasure_map.append(list(sys.stdin.readline().strip()))

    max_distance = 0
    for y, row in enumerate(treasure_map):
        for x, element in enumerate(row):
            if element == "L":
                visited = [[0 for _ in range(width)] for _ in range(height)]
                open_set = deque()
                open_set.append((0, y, x))
                visited[y][x] = 1

                while open_set:
                    cur_element = open_set.popleft()
                    cur_distance = cur_element[0]
                    cur_y = cur_element[1]
                    cur_x = cur_element[2]

                    max_distance = max(max_distance, cur_distance)

                    for d in direction:
                        next_y = d[0] + cur_y
                        next_x = d[1] + cur_x
                        if 0 <= next_y < height and 0 <= next_x < width:
                            if treasure_map[next_y][next_x] == "L" and not visited[next_y][next_x]:
                                visited[next_y][next_x] = 1
                                open_set.append((cur_distance + 1, next_y, next_x))

    print(max_distance)
