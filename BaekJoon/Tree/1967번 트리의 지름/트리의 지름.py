import sys

sys.setrecursionlimit(100000)
adj_list = []
visited = []
node_diameter = []


def bfs(node):
    visited[node] = 1
    # leaf 일때
    if not adj_list[node]:
        return 0

    max_weight = 0
    for next_node in adj_list[node]:
        if not visited[next_node[0]]:
            node_weight = next_node[1] + bfs(next_node[0])
            node_diameter[node].append(node_weight)
            if max_weight < node_weight:
                max_weight = node_weight
    return max_weight


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    if N == 1:
        print(0)
    else:
        visited = [0 for _ in range(N + 1)]
        node_diameter = [[] for _ in range(N + 1)]
        adj_list = [[] for _ in range(N+1)]

        for _ in range(N - 1):
            node1, node2, weight = map(int, sys.stdin.readline().split())
            adj_list[node1].append([node2, weight])
            adj_list[node2].append([node1, weight])

        bfs(1)

        max_diameter = 0
        for weights in node_diameter:
            if len(weights) >= 2:
                first_max = weights.pop(weights.index(max(weights)))
                second_max = weights.pop(weights.index(max(weights)))
                diameter = first_max + second_max
            elif len(weights) == 1:
                diameter = weights.pop()
            else:
                diameter = 0
            if diameter > max_diameter:
                max_diameter = diameter
        print(max_diameter)
