# 거듭제곱법을 이용한 풀이

import sys

if __name__ == '__main__':
    K, P, N = map(int, sys.stdin.readline().split())
    divisor = 1000000007
    exp = str(bin(N)[2:])
    dp = [0 for _ in range(len(exp))]

    for i in range(len(dp)):
        if i == 0:
            dp[0] = P % divisor
        else:
            dp[i] = (dp[i - 1] * dp[i - 1]) % divisor

    result = 1
    for i, ch in enumerate(reversed(exp)):
        if ch == '1':
            result *= dp[i]
    result = result % divisor
    result = (K % divisor * result) % divisor
    print(result)