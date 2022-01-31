if __name__ == '__main__':
    N, K = map(int, input().split())
    prime_list = [False, False] + [True] * (N - 1)

    cnt = 0
    for i in range(2, N + 1):
        if prime_list[i]:
            for j in range(i, N+1, i):
                if prime_list[j]:
                    prime_list[j] = False
                    cnt += 1
                    if cnt == K:
                        print(j)
                        exit(0)