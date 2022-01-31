import sys


class Heap:
    def __init__(self):
        self.min_heap = []

    def insert(self, key):
        self.min_heap.append(key)
        idx = len(self.min_heap) - 1
        while idx > 0 and self.min_heap[int((idx - 1) / 2)] > self.min_heap[idx]:
            tmp = self.min_heap[int((idx - 1) / 2)]
            self.min_heap[int((idx - 1) / 2)] = self.min_heap[idx]
            self.min_heap[idx] = tmp
            idx = int((idx - 1) / 2)

    def pop_heap(self):
        if len(self.min_heap) > 1:
            min_value = self.min_heap[0]
            self.min_heap[0] = self.min_heap.pop()
            here = 0
            length = len(self.min_heap)
            while True:
                left = here * 2 + 1
                right = here * 2 + 2
                if left >= length:
                    break

                next_idx = here
                # 부모와 왼쪽 자식과 비교하고 왼쪽 자식이 더 작다면 넣기
                if self.min_heap[here] > self.min_heap[left]:
                    next_idx = left
                # 만약 오른쪽 자식이 있다면 왼쪽 자식과 비교후에 오른쪽 자식이 더 작다면 바꾸기
                if right < length and self.min_heap[next_idx] > self.min_heap[right]:
                    next_idx = right

                if next_idx == here:
                    break

                tmp = self.min_heap[next_idx]
                self.min_heap[next_idx] = self.min_heap[here]
                self.min_heap[here] = tmp

                here = next_idx
            return min_value
        else:
            return self.min_heap.pop()


if __name__ == '__main__':
    heap = Heap()
    N = int(sys.stdin.readline())
    result = []
    for _ in range(N):
        cmd = int(sys.stdin.readline())
        if cmd != 0:
            heap.insert(cmd)
        else:
            if len(heap.min_heap) > 0:
                result.append(heap.pop_heap())
            else:
                result.append(0)

    print(*result, sep='\n')
