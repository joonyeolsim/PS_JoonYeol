if __name__ == '__main__':
    N = int(input())
    if N == 1:
        print(0)
    else:
        nums = [1 for i in range(N+1)]
        prime_nums = []
        # 에라토스테네스의 체
        for i in range(2, N+1):
            if nums[i]:
                prime_nums.append(i)
                for j in range(i, N+1, i):
                    nums[j] = 0
        start = 0
        end = 0
        prime_nums_len = len(prime_nums)
        prime_sum = 0
        result = 0

        while True:
            if prime_sum >= N:
                if prime_sum == N:
                    result += 1
                prime_sum -= prime_nums[start]
                start += 1
            else:
                if end == prime_nums_len:
                    prime_sum -= prime_nums[start]
                    start += 1
                else:
                    prime_sum += prime_nums[end]
                    end += 1

            if start == end:
                break
        print(result)