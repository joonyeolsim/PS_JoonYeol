from collections import deque

if __name__ == '__main__':
    balloon_num = int(input())
    balloon_queue = deque([i + 1, gap] for i, gap in enumerate(map(int, input().split())))
    pop_order = []
    last_value = 1

    for _ in range(balloon_num):
        value_in_balloon = balloon_queue.popleft()
        pop_order.append(value_in_balloon[0])
        if last_value * value_in_balloon[1] < 0:
            balloon_queue.reverse()

        balloon_queue.rotate(1 - abs(value_in_balloon[1]))  # -(abs(value_in_balloon[1]) - 1)
        last_value = value_in_balloon[1]
    print(*pop_order, sep=' ')
