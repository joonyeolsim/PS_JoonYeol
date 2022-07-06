if __name__ == '__main__':
    N = int(input())
    time_list = list(map(int, input().split()))

    time_list.sort()
    time_sum = 0
    accumulate_time = 0
    for time in time_list:
        accumulate_time += time
        time_sum += accumulate_time
    print(time_sum)