if __name__ == '__main__':
    N, M = map(int, input().split())

    chess_board = []
    for _ in range(N):
        chess_board.append(input())

    cnt_list = []
    for row in range(N - 7):
        for col in range(M - 7):
            cnt1 = 0
            cnt2 = 0
            for i in range(row, row + 8):
                for j in range(col, col + 8):
                    if (i + j) % 2 == 0:
                        if chess_board[i][j] == 'W':
                            cnt1 += 1
                        if chess_board[i][j] == 'B':
                            cnt2 += 1
                    else:
                        if chess_board[i][j] == 'B':
                            cnt1 += 1
                        if chess_board[i][j] == 'W':
                            cnt2 += 1
            cnt_list.append(cnt1)
            cnt_list.append(cnt2)
    print(min(cnt_list))

