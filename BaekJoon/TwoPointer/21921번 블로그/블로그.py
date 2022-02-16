if __name__ == '__main__':
    N, X = map(int, input().split())
    view_counts = list(map(int, input().split()))
    max_view_count = 0
    period_count = 0
    partial_sum = 0

    for i in range(X - 1):
        partial_sum += view_counts[i]

    for i in range(X - 1, N):
        partial_sum += view_counts[i]
        if partial_sum >= max_view_count:
            max_view_count = partial_sum
            period_count += 1
        partial_sum -= view_counts[i-X+1]

    if max_view_count == 0:
        print("SAD")
    else:
        print(max_view_count)
        print(period_count)
