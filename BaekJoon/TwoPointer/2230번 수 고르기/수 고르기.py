import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    nums = []
    min_difference = float("inf")
    for i in range(N):
        nums.append(int(sys.stdin.readline().rstrip()))

    nums.sort()
    start = 0
    end = 1

    while start < end:
        difference = nums[end] - nums[start]
        if difference >= M:
            if min_difference > difference:
                min_difference = difference
            start += 1
            if start == end and end != N - 1:
                end += 1
        else:
            if end == N - 1:
                start += 1
            else:
                end += 1

    print(min_difference)