# 무방향 인접 행렬
# bfs 탐색
def bfs(graph, start):
    visited = [False] * len(graph)
    answer = []

    queue = [start]
    visited[start] = True

    while queue:
        node = queue.pop(0)
        answer.append(node)
        for i in range(len(graph[node])):
            if graph[node][i] == 1 and not visited[i] and node != i:
                queue.append(i)
                visited[i] = True
    return answer


if __name__ == '__main__':
    city_num = int(input())
    itinerary_num = int(input())
    city_map = []
    result = "NO"
    possible_citys = []

    for i in range(city_num):
        city_map.append(list(map(int, input().split())))

    remain_city_list = list(range(city_num))
    for i in range(city_num):
        if i in remain_city_list:
            possible_city = bfs(city_map, i)
            remain_city_list = [city for city in remain_city_list if city not in possible_city]
            possible_citys.append(possible_city)

    itinerary = list(map(int, input().split()))
    for index, _ in enumerate(itinerary):
        itinerary[index] = itinerary[index] - 1
    itinerary = set(itinerary)

    for possible_city in possible_citys:
        set_possible_city = set(possible_city)
        if itinerary.issubset(possible_city):
            result = "YES"
    print(result)
