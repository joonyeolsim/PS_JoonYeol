if __name__ == '__main__':
    num_list = [0 for i in range(7)]

    dice = list(map(int, input().split()))

    for dice_num in dice:
        num_list[dice_num] += 1

    if 3 in num_list:
        print(10000 + num_list.index(3) * 1000)
    elif 2 in num_list:
        print(1000 + num_list.index(2) * 100)
    else:
        print((6 - num_list[::-1].index(1)) * 100)