import sys


def paint(house, prev_paint):
    if house == N:
        return 0

    min_paint_cost = float("inf")
    for next_paint in range(3):
        if prev_paint == next_paint:
            continue

        if dp[house][next_paint]:
            paint_cost = dp[house][next_paint]
        else:
            paint_cost = costs[house][next_paint] + paint(house + 1, next_paint)
            dp[house][next_paint] = paint_cost
        min_paint_cost = min(min_paint_cost, paint_cost)

    return min_paint_cost


N = int(sys.stdin.readline().strip())
dp = [[0 for _ in range(3)] for _ in range(N)]
costs = []

for _ in range(N):
    costs.append(list(map(int, sys.stdin.readline().split())))

print(paint(0, -1))
