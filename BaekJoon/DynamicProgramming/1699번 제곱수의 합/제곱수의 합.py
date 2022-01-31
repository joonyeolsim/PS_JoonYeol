if __name__ == '__main__':
    N = int(input())
    dp = [i for i in range(N+1)]
    dp[1] = 1
    for i in range(2, N + 1):
        square_root = 1
        while square_root ** 2 <= i:
            if dp[i] > dp[i - square_root ** 2] + 1:
                dp[i] = dp[i - square_root ** 2] + 1
            square_root += 1
    print(dp[N])
