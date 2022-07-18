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


def dijkstra(start_idx):
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
                elif status[i] == 'F' and distance[i] > (distance[next_idx] + graph[i][next_idx]):
                    distance[i] = distance[next_idx] + graph[i][next_idx]


if __name__ == '__main__':
    N, E = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    for _ in range(E):
        node1, node2, edge_weight = map(int, sys.stdin.readline().split())
        graph[node1][node2] = edge_weight
        graph[node2][node1] = edge_weight

    v1, v2 = map(int, sys.stdin.readline().split())

    path1_sum = 0
    path2_sum = 0

    dijkstra(1)
    path1_sum += distance[v1]
    path2_sum += distance[v2]

    dijkstra(v1)
    path1_sum += distance[v2]
    path2_sum += distance[v2]
    path2_sum += distance[N]

    dijkstra(v2)
    path1_sum += distance[N]

    if path1_sum == math.inf and path2_sum == math.inf:
        print(-1)
    else:
        print(min(path1_sum, path2_sum))