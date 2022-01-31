if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        i_sum = 0
        j = i
        while j != 0:
            i_sum += j % 10
            j = j // 10
        if i_sum + i == N:
            print(i)
            exit(0)
    print(0)
