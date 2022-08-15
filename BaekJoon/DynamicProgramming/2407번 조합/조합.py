import sys


def combination(n, m):
    if n == m or m == 0:
        return 1
    if dp[n][m]:
        return dp[n][m]

    dp[n][m] = combination(n - 1, m - 1) + combination(n - 1, m)
    return dp[n][m]


N, M = map(int, sys.stdin.readline().split())
dp = [[0 for _ in range(101)] for _ in range(101)]
print(combination(N, M))