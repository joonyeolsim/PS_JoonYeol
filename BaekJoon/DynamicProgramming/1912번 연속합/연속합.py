import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().split()))

    dp = nums[:]

    for i in range(1, N):
        dp[i] = max(dp[i], dp[i-1] + nums[i])

    print(max(dp))
