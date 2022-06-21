import sys
from copy import deepcopy
from itertools import combinations

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
virus_coordinate = []
N = 0
M = 0


def bfs(_lab):
    open_set = []
    open_set.extend(virus_coordinate)

    while open_set:
        virus = open_set.pop(0)
        for direction in directions:
            next_y = virus[0] + direction[0]
            next_x = virus[1] + direction[1]
            if 0 <= next_y < N and 0 <= next_x < M:
                if _lab[next_y][next_x] == 0:
                    _lab[next_y][next_x] = 2
                    open_set.append((next_y, next_x))
    return _lab


def score_lab(_lab):
    _score = 0
    for _lab_vector in _lab:
        for _element in _lab_vector:
            if _element == 0:
                _score += 1
    return _score


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    max_score = 0
    lab = []
    empty_coordinate = []

    for _ in range(N):
        lab.append(list(map(int, sys.stdin.readline().split())))

    for y, lab_vector in enumerate(lab):
        for x, element in enumerate(lab_vector):
            if element == 2:
                virus_coordinate.append((y, x))
            elif element == 0:
                empty_coordinate.append((y, x))

    for build_walls_coordinate in list(combinations(empty_coordinate, 3)):
        temp_lab = deepcopy(lab)
        for build_wall_coordinate in build_walls_coordinate:
            temp_lab[build_wall_coordinate[0]][build_wall_coordinate[1]] = 1
        virus_spread_lab = bfs(temp_lab)
        score = score_lab(virus_spread_lab)
        if score > max_score:
            max_score = score

    print(max_score)