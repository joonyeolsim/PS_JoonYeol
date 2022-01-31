import heapq
import sys

if __name__ == '__main__':
    heap = []
    N = int(input())
    for _ in range(N):
        num = int(sys.stdin.readline().rstrip())
        if num:
            heapq.heappush(heap, (abs(num), num))
        else:
            if heap:
                print(heapq.heappop(heap)[1])
            else:
                print(0)

