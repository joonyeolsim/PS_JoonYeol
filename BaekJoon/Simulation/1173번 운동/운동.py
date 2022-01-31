if __name__ == '__main__':
    N, m, M, T, R = map(int, input().split())
    X = m
    total_time = 0

    if M - m < T:
        print(-1)
        exit(0)

    while N:
        if X + T <= M:
            X += T
            N -= 1
        else:
            if X - R >= m:
                X -= R
            else:
                X = m

        total_time += 1
    print(total_time)
