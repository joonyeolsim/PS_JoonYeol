dp = [0, 1, 2] + [0 for _ in range(1000)]


def solve(n):
    if dp[n]:
        return dp[n]

    dp[n] = (solve(n - 1) + solve(n - 2)) % 10007
    return dp[n]


N = int(input())
print(solve(N))
