import sys


class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, num):
        self.stack_list.append(num)

    def pop(self):
        if self.stack_list:
            return self.stack_list.pop()
        return -1

    def size(self):
        return len(self.stack_list)

    def empty(self):
        if self.stack_list:
            return 0
        return 1

    def top(self):
        if self.stack_list:
            return self.stack_list[-1]
        return -1


if __name__ == '__main__':
    instruction_cnt = int(input())
    result_list = []
    stack = Stack()

    for i in range(instruction_cnt):
        instruction = sys.stdin.readline().rstrip().split()
        inst = instruction[0]
        func_to_run = getattr(stack, inst)
        if inst == "push":
            func_to_run(instruction[1])
        else:
            result_list.append(func_to_run())

    for result in result_list:
        print(result)