if __name__ == '__main__':
    start = 1
    N = int(input())
    end = N
    result = 0

    while start <= end:
        mid = (start+end) // 2
        if N < ((mid * (mid + 1)) / 2):
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    print(result)
