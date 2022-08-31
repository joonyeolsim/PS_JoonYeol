from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())

open_list = deque()
visited = [0 for _ in range(100001)]

open_list.append((0, N))
time = 0

while open_list:
    time, dot = open_list.popleft()
    visited[dot] = 1
    time += 1

    if dot == K:
        print(time - 1)
        break

    if 0 <= dot - 1 and not visited[dot - 1]:
        open_list.append((time, dot - 1))

    if dot + 1 <= 100000 and not visited[dot + 1]:
        open_list.append((time, dot + 1))

    if dot * 2 <= 100000 and not visited[dot * 2]:
        open_list.append((time, dot * 2))