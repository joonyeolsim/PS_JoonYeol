from collections import deque

if __name__ == '__main__':
    queue = deque()
    N = int(input())
    for i in range(1, N + 1):
        queue.append(i)

    while queue:
        print(queue.popleft(), end=" ")
        if queue:
            queue.append(queue.popleft())
