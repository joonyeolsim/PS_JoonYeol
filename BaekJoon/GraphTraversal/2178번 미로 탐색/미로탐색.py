import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    maze = []
    for _ in range(N):
        maze.append(list(map(int, sys.stdin.readline().rstrip())))
    candidate_nodes = []
    visited = [[0 for _ in range(M)] for _ in range(N)]
    open_set = [{
        'y': 0,
        'x': 0,
        'count': 1,
    }]
    visited[0][0] = 1

    while open_set:
        node = open_set.pop(0)
        y, x = node['y'], node['x']
        count = node['count']

        if y == N - 1 and x == M - 1:
            print(count)
            break
        if y - 1 >= 0 and maze[y - 1][x] == 1 and visited[y - 1][x] == 0:
            candidate_nodes.append([y - 1, x])
        if y + 1 < N and maze[y + 1][x] == 1 and visited[y + 1][x] == 0:
            candidate_nodes.append([y + 1, x])
        if x - 1 >= 0 and maze[y][x - 1] == 1 and visited[y][x - 1] == 0:
            candidate_nodes.append([y, x - 1])
        if x + 1 < M and maze[y][x + 1] == 1 and visited[y][x + 1] == 0:
            candidate_nodes.append([y, x + 1])

        for candidate_node in candidate_nodes:
            visited[candidate_node[0]][candidate_node[1]] = 1

            open_set.append({
                'y': candidate_node[0],
                'x': candidate_node[1],
                'count': count + 1
            })

        candidate_nodes.clear()
