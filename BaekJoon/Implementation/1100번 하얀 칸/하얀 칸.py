import sys

if __name__ == '__main__':
    chessboard = []
    count = 0

    for _ in range(8):
        chessboard.append(sys.stdin.readline().rstrip())

    for i in range(8):
        for j in range(8):
            if chessboard[i][j] == 'F' and (i + j) % 2 == 0:
                count += 1
    print(count)
