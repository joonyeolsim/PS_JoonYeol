import sys

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    coin_list = []

    for _ in range(N):
        coin_list.append(int(sys.stdin.readline().strip()))

    coin_list.sort(reverse=True)
    coin_cnt = 0

    while K:
        for coin in coin_list:
            if K - coin >= 0:
                K -= coin
                coin_cnt += 1
                break

    print(coin_cnt)
