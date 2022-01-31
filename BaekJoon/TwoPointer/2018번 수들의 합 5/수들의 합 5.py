if __name__ == '__main__':
    N = int(input())
    arr = range(1, N+1)

    now, end = 0, 0
    ans = 0
    for start in range(N):
        while end < N and now < N:
            now += arr[end]
            end += 1
        if now == N:
            ans += 1
        now -= arr[start]
    print(ans)