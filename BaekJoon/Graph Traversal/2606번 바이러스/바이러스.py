import sys


def bfs(start_node, _adj_list, _visited):
    count = 0
    next_nodes = [start_node]
    _visited[start_node] = 1
    while next_nodes:
        current_node = next_nodes.pop(0)
        for node in adj_list[current_node]:
            if not _visited[node]:
                next_nodes.append(node)
                _visited[node] = 1
                count += 1
    return count


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    E = int(sys.stdin.readline().rstrip())

    adj_list = [[] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]

    for _ in range(E):
        node1, node2 = map(int, sys.stdin.readline().split())
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)
    print(bfs(1, adj_list, visited))
