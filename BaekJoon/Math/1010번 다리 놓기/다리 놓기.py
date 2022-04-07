dp = []


def combinations(n, r):
    # 이미 구한 값이라면
    if dp[n][r] > 0:
        return dp[n][r]

    # base case
    if r == 0 or n == r:
        dp[n][r] = 1
        return dp[n][r]

    # combinations 구하기
    dp[n][r] = combinations(n - 1, r - 1) + combinations(n - 1, r)

    return dp[n][r]


if __name__ == '__main__':
    T = int(input())
    dp = [[0 for _ in range(30)] for _ in range(30)]
    for _ in range(T):
        N, M = map(int, input().split())
        print(combinations(M, N))