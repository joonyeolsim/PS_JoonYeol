# bfs 알고리즘

import sys
from collections import deque

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    adj_matrix = []
    for _ in range(N):
        row = list(map(int, sys.stdin.readline().strip()))
        adj_matrix.append(row)

    visited = [[False for _ in range(N)] for _ in range(N)]
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    block_nums = []

    for y in range(N):
        for x in range(N):
            if adj_matrix[y][x] and not visited[y][x]:
                block_num = 1
                open_set = deque()
                open_set.append((y, x))
                visited[y][x] = True
                while open_set:
                    cur_y, cur_x = open_set.popleft()
                    for dy, dx in direction:
                        next_y = cur_y + dy
                        next_x = cur_x + dx
                        if 0 <= next_y < N and 0 <= next_x < N and adj_matrix[next_y][next_x] and not visited[next_y][next_x]:
                            open_set.append((next_y, next_x))
                            visited[next_y][next_x] = True
                            block_num += 1
                block_nums.append(block_num)
    block_nums.sort()
    print(len(block_nums))
    print(*block_nums, sep='\n')