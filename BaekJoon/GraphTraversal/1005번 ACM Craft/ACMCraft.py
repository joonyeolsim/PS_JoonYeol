import sys

adj_list = []
build_times = []
visited = []


def dfs(building):
    if not adj_list[building]:
        return build_times[building]

    max_time = 0
    for next_building in adj_list[building]:
        if visited[next_building] == -1:
            time = dfs(next_building)
            max_time = max(time, max_time)
        else:
            max_time = max(visited[next_building], max_time)
    visited[building] = max_time + build_times[building]
    return max_time + build_times[building]


if __name__ == '__main__':
    sys.setrecursionlimit(110000)
    T = sys.stdin.readline().strip()
    for _ in range(int(T)):
        N, K = map(int, sys.stdin.readline().split())
        adj_list = [[] for _ in range(N + 1)]
        visited = [-1 for _ in range(N + 1)]
        build_times = [0] + list(map(int, sys.stdin.readline().split()))
        for _ in range(K):
            i, j = map(int, sys.stdin.readline().split())
            adj_list[j].append(i)

        w = int(sys.stdin.readline().strip())
        print(dfs(w))