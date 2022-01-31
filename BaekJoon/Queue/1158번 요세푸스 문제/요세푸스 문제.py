from collections import deque


# 환형 연결 리스트
class Node:
    def __init__(self, number):
        self.number = number
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = Node('head')
        self.head.next = self.head
        self.cur_node = self.head

    def insert(self, item, new):
        new_node = Node(new)
        cur_node = self.find(item)
        new_node.next = cur_node.next
        cur_node.next = new_node

    def find(self, item):
        cur_node = self.head
        while cur_node.number != item:
            cur_node = cur_node.next
        return cur_node

    def find_previous(self, item):
        cur_node = self.head
        while cur_node.next.number != item:
            cur_node = cur_node.next
        return cur_node

    def print(self):
        cur_node = self.head
        while cur_node.next.number != 'head':
            print(cur_node.number, end=' -> ')
            cur_node = cur_node.next
        print(cur_node.number)

    def remove(self, gap):
        cnt = 0
        while cnt < gap:
            self.cur_node = self.cur_node.next
            if self.cur_node.number != 'head':
                cnt += 1
        prev_node = self.find_previous(self.cur_node.number)
        prev_node.next = prev_node.next.next
        return str(self.cur_node.number)


if __name__ == '__main__':
    N, K = map(int, input().split())

    # 스택 해결
    people_queue = deque([i+1 for i in range(N)])
    index = 0
    print('<', end='')
    for i in range(N - 1):
        for _ in range(K - 1):
            people_queue.append(people_queue.popleft())
        print(f'{people_queue.popleft()}, ', end='')
    print(f'{people_queue.popleft()}>', end='')

    # 환형 연결 리스트
    # people_list = CircularLinkedList()
    # people_list.insert('head', 1)
    # for i in range(2, N + 1):
    #     people_list.insert(i - 1, i)
    #
    # print("<", end='')
    # for i in range(N - 1):
    #     print(people_list.remove(K), end=', ')
    # print(people_list.remove(K), end='')
    # print(">")