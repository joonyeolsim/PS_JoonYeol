import sys
import collections


class Queue:
    def __init__(self):
        self.queue = collections.deque()

    def push_front(self, num):
        self.queue.appendleft(num)

    def push_back(self, num):
        self.queue.append(num)

    def pop_front(self):
        if self.queue:
            return self.queue.popleft()
        return -1

    def pop_back(self):
        if self.queue:
            return self.queue.pop()
        return -1

    def size(self):
        return len(self.queue)

    def empty(self):
        if self.queue:
            return 0
        return 1

    def front(self):
        if self.queue:
            return self.queue[0]
        return -1

    def back(self):
        if self.queue:
            return self.queue[-1]
        return -1


if __name__ == '__main__':
    instruction_cnt = int(input())
    result_list = []
    queue = Queue()

    for i in range(instruction_cnt):
        instruction = sys.stdin.readline().rstrip().split()
        inst = instruction[0]
        func_to_run = getattr(queue, inst)
        if "push" in inst:
            func_to_run(instruction[1])
        else:
            result_list.append(func_to_run())

    for result in result_list:
        print(result)
