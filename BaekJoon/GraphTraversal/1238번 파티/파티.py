import sys
import math

status = []
distance = []
tree = []
fringe = []


def get_min_distance_idx():
    min_distance = math.inf
    min_idx = 0
    fringe_idx_ = 0
    for f, idx in enumerate(fringe):
        if min_distance > distance[idx]:
            min_distance = distance[idx]
            min_idx = idx
            fringe_idx_ = f

    return min_idx, fringe_idx_


def dijkstra(graph, start_idx):
    global status, distance, tree, fringe
    status = ['U' for _ in range(N + 1)]
    distance = [math.inf for _ in range(N + 1)]
    tree = []
    fringe = []

    tree.append(start_idx)
    status[start_idx] = 'T'
    distance[start_idx] = 0

    for i, weight in enumerate(graph[start_idx]):
        if weight > 0:
            fringe.append(i)
            status[i] = 'F'
            distance[i] = weight

    while fringe:
        # 가장 가까운 값의 노드를 트리에 추가
        next_idx, fringe_idx = get_min_distance_idx()
        tree.append(next_idx)
        status[next_idx] = 'T'
        fringe.pop(fringe_idx)

        for i, weight in enumerate(graph[next_idx]):
            # 연결된 것들 중에서
            if weight > 0:
                # fringe에 없다면 update
                if status[i] == 'U':
                    fringe.append(i)
                    status[i] = 'F'
                    distance[i] = distance[next_idx] + weight

                # 현재 경로보다 더 짧은 경로라면 업데이트
                elif status[i] == 'F' and distance[i] > (distance[next_idx] + graph[next_idx][i]):
                    distance[i] = distance[next_idx] + graph[next_idx][i]


if __name__ == '__main__':
    N, M, X = map(int, sys.stdin.readline().split())
    graph1 = [[0 for _ in range(N + 1)] for _ in range(N + 1)] # 파티로 가는길
    graph2 = [[0 for _ in range(N + 1)] for _ in range(N + 1)] # 집에 돌아오는 길
    distance_sum = [0 for _ in range(N + 1)]

    for _ in range(M):
        node1, node2, edge_weight = map(int, sys.stdin.readline().split())
        graph1[node2][node1] = edge_weight
        graph2[node1][node2] = edge_weight

    dijkstra(graph1, X)
    for i in range(N + 1):
        distance_sum[i] += distance[i]
    dijkstra(graph2, X)
    for i in range(N + 1):
        distance_sum[i] += distance[i]
    print(max(distance_sum[1:]))
