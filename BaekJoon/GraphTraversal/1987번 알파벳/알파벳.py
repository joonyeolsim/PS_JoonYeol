import sys

max_count = 0
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
alphabets = [0 for i in range(26)]
tiles = []
R = 0
C = 0


def dfs(y, x, count):
    global max_count

    max_count = max(max_count, count + 1)
    for d in directions:
        next_y = y + d[0]
        next_x = x + d[1]

        if 0 <= next_y < R and 0 <= next_x < C:
            alpha_idx = ord(tiles[next_y][next_x]) - 65
            if not alphabets[alpha_idx]:
                alphabets[alpha_idx] = 1
                dfs(next_y, next_x, count + 1)
                alphabets[alpha_idx] = 0


if __name__ == '__main__':
    R, C = map(int, sys.stdin.readline().split())

    for _ in range(R):
        tiles.append(list(map(str, sys.stdin.readline()[:-1])))

    alphabets[ord(tiles[0][0]) - 65] = 1
    dfs(0, 0, 0)
    print(max_count)
