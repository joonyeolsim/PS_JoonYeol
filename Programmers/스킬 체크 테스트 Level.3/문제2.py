import heapq


def solution(operations):
    answer = [0, 0]
    max_heap = []
    min_heap = []
    for op in operations:
        str_op, num = op.split()
        num = int(num)
        if str_op == "I":
            heapq.heappush(min_heap, [num, num])
            heapq.heappush(max_heap, [-num, num])
        else:
            if num == 1:
                if max_heap:
                    max_num = heapq.heappop(max_heap)
                    max_num[0] = -max_num[0]
                    min_heap.remove(max_num)
            else:
                if min_heap:
                    min_num = heapq.heappop(min_heap)
                    min_num[0] = -min_num[0]
                    max_heap.remove(min_num)
    if max_heap:
        answer = [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)[1]]
    return answer


if __name__ == '__main__':
    print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))