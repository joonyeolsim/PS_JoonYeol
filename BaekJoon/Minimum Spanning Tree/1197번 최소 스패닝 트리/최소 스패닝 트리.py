import sys
from collections import deque

if __name__ == '__main__':
    INF = 2147483648
    V, E = map(int, sys.stdin.readline().split())

    node_status = ['U' for _ in range(V + 1)]
    node_distance = [INF for _ in range(V + 1)]
    adj = [[] for _ in range(V + 1)]

    # 안쓰는 값 초기화
    node_status[0] = 'N'
    node_distance[0] = 0

    # 인접 리스트 받기
    for i in range(E):
        v1, v2, d = map(int, sys.stdin.readline().split())
        adj[v1].append((v2, d))
        adj[v2].append((v1, d))

    node_status[1] = 'T'
    node_distance[1] = 0
    for adj_node in adj[1]:
        node_status[adj_node[0]] = 'F'
        node_distance[adj_node[0]] = adj_node[1]

    while 'F' in node_status:
        next_index = 0
        min_distance = INF
        # 제일 짧은 가중치 찾기
        for i, d in enumerate(node_distance):
            if node_status[i] == 'F' and min_distance > d:
                next_index = i
                min_distance = d
        # 트리에 편입
        node_status[next_index] = 'T'

        # 편입된 노드와 인접한 노드 처리
        for adj_node in adj[next_index]:
            # replace U to F
            if node_status[adj_node[0]] == 'U':
                node_status[adj_node[0]] = 'F'
            # decrease key
            if adj_node[1] < node_distance[adj_node[0]] and node_status[adj_node[0]] == 'F':
                node_distance[adj_node[0]] = adj_node[1]

    print(sum(node_distance))