import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())

    bomb_board = []
    for _ in range(n):
        bomb_board.append(list(sys.stdin.readline().strip()))

    user_board = []
    for _ in range(n):
        user_board.append(list(sys.stdin.readline().strip()))

    directions = [(0, 1),
                  (0, -1),
                  (1, 0),
                  (-1, 0),
                  (1, 1),
                  (1, -1),
                  (-1, 1),
                  (-1, -1)
                  ]
    result_board = [['.' for _ in range(n)] for _ in range(n)]
    bomb_flag = False
    for i in range(n):
        for j in range(n):
            # 지뢰가 없으면서 열린 칸
            if bomb_board[i][j] != '*' and user_board[i][j] == 'x':
                bomb_count = 0
                for d in directions:
                    next_x = i + d[0]
                    next_y = j + d[1]
                    if 0 <= next_x < n and 0 <= next_y < n:
                        if bomb_board[next_x][next_y] == '*':
                            bomb_count += 1
                result_board[i][j] = bomb_count
            # 지뢰가 있으면서 열린 칸
            if bomb_board[i][j] == '*' and user_board[i][j] == 'x':
                bomb_flag = True

    if bomb_flag:
        for i in range(n):
            for j in range(n):
                if bomb_board[i][j] == '*':
                    result_board[i][j] = '*'

    for row in result_board:
        print(*row, sep='')
