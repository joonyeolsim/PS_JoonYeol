import sys


if __name__ == '__main__':
    sys.setrecursionlimit(10001)
    N, M = map(int, sys.stdin.readline().split())
    cache = [0 for _ in range(10001)]

    for _ in range(N):
        V, C, K = map(int, sys.stdin.readline().split())
        square_num = 1
        temp = 0
        while K > 0:
            temp = min(K, square_num)
            for i in range(M, V * temp - 1, -1):
                cache[i] = max(cache[i - V * temp] + C * temp, cache[i])
            square_num *= 2
            K -= temp

    print(max(cache))
