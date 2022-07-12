if __name__ == '__main__':
    num_list = [0 for _ in range(9)]
    room_num = int(input())
    cnt = 0
    for i in range(len(num_list)):
        num_list[i] += 1
    cnt += 1
    num_list[6] += 1
    while room_num:
        next_num = room_num % 10
        if next_num == 9:
            next_num = 6
        num_list[next_num] -= 1
        if num_list[next_num] < 0:
            for i in range(len(num_list)):
                num_list[i] += 1
            num_list[6] += 1
            cnt += 1
        room_num = room_num // 10
    print(cnt)
