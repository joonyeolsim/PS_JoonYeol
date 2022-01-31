if __name__ == '__main__':
    board = input()

    now = 0
    while now < len(board):
        if board[now] == '.':
            now += 1
            continue

        if board[now:now+4] == "XXXX":
            board = "".join((board[:now], "AAAA", board[now+4:]))
            now += 4

        elif board[now:now+2] == "XX":
            board = "".join((board[:now], "BB", board[now+2:]))
            now += 2

        else:
            now = -1
            break

    if now == -1:
        print(-1)
    else:
        print(board)

