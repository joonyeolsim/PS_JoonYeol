import sys


if __name__ == '__main__':
    N = 10000
    sieve = [False, False] + [True] * (N - 1)
    prime = []
    goldbach = {}
    # 10000까지의 모든 소수 찾기
    for i in range(2, N):
        if sieve[i]:
            prime.append(i)
            for j in range(i + i, N + 1, i):
                sieve[j] = False

    for i in prime:
        for j in prime:
            gold_num = i + j
            if gold_num in goldbach.keys():
                if abs(goldbach[gold_num][0] - goldbach[gold_num][1]) > abs(i - j):
                    goldbach[gold_num] = (i, j)
            else:
                goldbach[gold_num] = (i, j)

    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        num = int(sys.stdin.readline().rstrip())
        print("{0} {1}".format(goldbach[num][0], goldbach[num][1]))
