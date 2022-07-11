import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        M, N, K = map(int, sys.stdin.readline().split())

        field = [[0 for _ in range(M)] for _ in range(N)]
        state = [['U' for _ in range(M)] for _ in range(N)]
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        warm = 0

        for _ in range(K):
            x, y = map(int, sys.stdin.readline().split())
            field[y][x] = 1

        for y in range(N):
            for x in range(M):
                if field[y][x] == 1 and state[y][x] == 'U':
                    warm += 1
                    open_set = {(y, x)}
                    while open_set:
                        cur_y, cur_x = open_set.pop()
                        state[cur_y][cur_x] = 'F'
                        for d in direction:
                            next_y = cur_y + d[0]
                            next_x = cur_x + d[1]
                            if 0 <= next_y < N and 0 <= next_x < M:
                                if state[next_y][next_x] == 'U' and field[next_y][next_x] == 1:
                                    open_set.add((next_y, next_x))
        print(warm)
