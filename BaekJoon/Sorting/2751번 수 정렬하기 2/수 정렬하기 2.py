import sys
import heapq

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    heap = []

    for _ in range(N):
        heapq.heappush(heap, int(sys.stdin.readline().rstrip()))

    while heap:
        print(heapq.heappop(heap))
