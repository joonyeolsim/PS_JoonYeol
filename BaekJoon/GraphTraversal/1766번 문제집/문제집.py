import sys
import heapq


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())

    incoming_edges = [set() for _ in range(N + 1)]
    outgoing_edges = [set() for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    heap = []

    # graph construct
    for _ in range(M):
        node1, node2 = map(int, sys.stdin.readline().split())
        outgoing_edges[node1].add(node2)
        incoming_edges[node2].add(node1)

    # find no incoming edge node
    for problem, incoming_edge in enumerate(incoming_edges[1:]):
        if not incoming_edge:
            heapq.heappush(heap, problem + 1)

    while heap:
        problem = heapq.heappop(heap)
        visited[problem] = True
        print(problem, end=" ")
        for next_problem in outgoing_edges[problem]:
            incoming_edges[next_problem] -= {problem}
            if not visited[next_problem] and not incoming_edges[next_problem]:
                heapq.heappush(heap, next_problem)
