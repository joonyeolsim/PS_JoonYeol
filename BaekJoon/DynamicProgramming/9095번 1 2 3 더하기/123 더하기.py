if __name__ == '__main__':
    dp = [0, 1, 2, 4]

    T = int(input())

    for i in range(4, 11):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

    for _ in range(T):
        num = int(input())
        print(dp[num])
