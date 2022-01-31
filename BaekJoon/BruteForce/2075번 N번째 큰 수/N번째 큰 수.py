import heapq
import sys


if __name__ == '__main__':
    N = int(input())
    min_heap = []
    for _ in range(N):
        row = map(int, sys.stdin.readline().rstrip().split())
        if not min_heap:
            for num in row:
                heapq.heappush(min_heap, num)
        else:
            for num in row:
                if min_heap[0] < num:
                    heapq.heappush(min_heap, num)
                    heapq.heappop(min_heap)
                    print(min_heap)
    print(min_heap[0])