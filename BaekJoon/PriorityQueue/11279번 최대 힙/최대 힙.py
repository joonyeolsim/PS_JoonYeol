import heapq
import sys

if __name__ == '__main__':
    N = int(input())
    max_heap = []
    result = []
    for _ in range(N):
        num = int(sys.stdin.readline().rstrip())
        if num > 0:
            heapq.heappush(max_heap, (-num, num))
        else:
            if max_heap:
                result.append(heapq.heappop(max_heap)[1])
            else:
                result.append(0)

    for res in result:
        print(res)