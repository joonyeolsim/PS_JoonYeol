import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    city = []
    visited = [[0 for _ in range(N)] for _ in range(N)]
    open_set = []
    result = []
    count = 0

    for _ in range(N):
        city.append(list(map(int, sys.stdin.readline().rstrip())))

    for i in range(N):
        for j in range(N):
            if city[i][j] == 1 and visited[i][j] == 0:
                open_set.append([i, j])
                visited[i][j] = 1
                count += 1

            while open_set:
                y, x = open_set.pop(0)
                if y - 1 >= 0 and city[y - 1][x] == 1 and visited[y - 1][x] == 0:
                    open_set.append([y - 1, x])
                    visited[y - 1][x] = 1
                    count += 1
                if y + 1 < N and city[y + 1][x] == 1 and visited[y + 1][x] == 0:
                    open_set.append([y + 1, x])
                    visited[y + 1][x] = 1
                    count += 1
                if x - 1 >= 0 and city[y][x - 1] == 1 and visited[y][x - 1] == 0:
                    open_set.append([y, x - 1])
                    visited[y][x - 1] = 1
                    count += 1
                if x + 1 < N and city[y][x + 1] == 1 and visited[y][x + 1] == 0:
                    open_set.append([y, x + 1])
                    visited[y][x + 1] = 1
                    count += 1
            if count > 0:
                result.append(count)
                count = 0
    print(len(result))
    print(*sorted(result), sep='\n')
