import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    nums = list()
    sum_num = 0
    min_num = 4000
    max_num = -4000
    count = [0] * 8001
    for _ in range(N):
        n = int(sys.stdin.readline().rstrip())
        nums.append(n)
        sum_num += n
        if n > max_num:
            max_num = n
        if n < min_num:
            min_num = n
        count[n + 4000] += 1

    # 산술 평균
    print(round(sum_num / N))

    # 중앙값
    print(sorted(nums)[N // 2])

    # 최빈값
    max_count_num = []
    max_count = max(count)
    for i, c in enumerate(count):
        if c == max_count:
            max_count_num.append(i - 4000)

    if len(max_count_num) >= 2:
        print(max_count_num[1])
    else:
        print(max_count_num[0])

    # 범위
    print(max_num - min_num)
