if __name__ == '__main__':
    early = 45
    hour, minute = input().split()
    hour = int(hour)
    minute = int(minute)

    remain_time = minute - early
    if remain_time < 0:
        hour -= 1
        minute = 60 + remain_time
    else:
        minute = minute - 45

    if hour < 0:
        hour = 23

    print(hour, minute)
