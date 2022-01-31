from collections import deque

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