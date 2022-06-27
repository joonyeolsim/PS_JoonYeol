if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))

    dp = [1 for _ in range(N)]

    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums[:i]):
            if num1 > num2:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))
