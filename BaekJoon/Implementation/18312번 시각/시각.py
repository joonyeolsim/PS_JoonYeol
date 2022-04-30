if __name__ == '__main__':
    n, k = input().split()
    n = int(n)
    hour = 0
    minute = 0
    second = 0
    count = 0

    while not (hour == n + 1 and minute == 0 and second == 0):
        time = str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(second).zfill(2)
        if k in time:
            count += 1
        second += 1
        if second == 60:
            minute += 1
            second = 0
            if minute == 60:
                hour += 1
                minute = 0
    print(count)