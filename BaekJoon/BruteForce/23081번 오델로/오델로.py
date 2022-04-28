import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    othello = []
    for _ in range(N):
        othello.append(list(sys.stdin.readline().strip()))

    direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    max_count = 0
    max_y = 0
    max_x = 0
    for y in range(N):
        for x in range(N):
            if othello[y][x] == '.':
                count = 0

                for i in range(8):
                    current_x = x
                    current_y = y
                    temp_cnt = 0
                    while 0 <= current_y + direction[i][0] < N and 0 <= current_x + direction[i][1] < N and \
                            othello[current_y + direction[i][0]][current_x + direction[i][1]] == 'W':
                        current_y += direction[i][0]
                        current_x += direction[i][1]
                        temp_cnt += 1
                    if 0 <= current_y + direction[i][0] < N and 0 <= current_x + direction[i][1] < N and \
                            othello[current_y + direction[i][0]][current_x + direction[i][1]] == 'B':
                        count += temp_cnt

                if max_count < count:
                    max_count = count
                    max_y = y
                    max_x = x
    if max_count:
        print(max_x, max_y)
        print(max_count)
    else:
        print("PASS")