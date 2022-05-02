def solution(n, edge):
    adj_list = [[] for _ in range(n + 1)]
    for e in edge:
        adj_list[e[0]].append(e[1])
        adj_list[e[1]].append(e[0])

    open_set = [1]
    visited = [0 for _ in range(n + 1)]
    distances = [0 for _ in range(n + 1)]
    visited[1] = 1
    distances[1] = 0
    while open_set:
        node = open_set.pop(0)
        for next_node in adj_list[node]:
            if not visited[next_node]:
                open_set.append(next_node)
                distances[next_node] = distances[node] + 1
                visited[next_node] = 1
    answer = distances.count(max(distances))
    return answer


if __name__ == '__main__':
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))