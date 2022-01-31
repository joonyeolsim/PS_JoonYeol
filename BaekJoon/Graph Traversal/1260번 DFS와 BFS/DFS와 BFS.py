# 엣지의 개수가 노드의 개수보다 많기 때문에 인접 행렬로 구현
import sys


def dfs(current_node, _adjacent_matrix, _node_state):
    print(current_node, end=' ')
    _node_state[current_node] = 'V'
    for node, connected in enumerate(_adjacent_matrix[current_node]):
        if connected and _node_state[node] == 'U':
            dfs(node, _adjacent_matrix, _node_state)
    _node_state[current_node] = 'F'


def bfs(start_node, _adjacent_matrix, _node_state):
    _node_state[start_node] = 'V'
    possible_node = [start_node]
    while possible_node:
        current_node = possible_node.pop(0)
        print(current_node, end=' ')
        for node, connected in enumerate(_adjacent_matrix[current_node]):
            if connected and _node_state[node] == 'U':
                possible_node.append(node)
                _node_state[node] = 'V'


if __name__ == '__main__':
    V, E, first_node = map(int, sys.stdin.readline().split())
    # 0번은 안쓰는 인덱스, 1번부터 시작
    adjacent_matrix = [[0] * (V + 1) for i in range(V + 1)]
    node_state = ['U' for i in range(V + 1)]

    for _ in range(E):
        node1, node2 = map(int, sys.stdin.readline().split())
        adjacent_matrix[node1][node2] = 1
        adjacent_matrix[node2][node1] = 1

    dfs(first_node, adjacent_matrix, node_state)
    print()
    node_state = ['U' for i in range(V + 1)]
    bfs(first_node, adjacent_matrix, node_state)
