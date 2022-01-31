import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    num_list = list(map(int, sys.stdin.readline().split()))
    num_index = dict()
    prev_num = 1000001
    index = 0

    for num in list(set(num_list)):
        if num == prev_num:
            continue
        else:
            num_index[num] = index
            prev_num = num
            index += 1

    for num in num_list:
        print(num_index[num], end=' ')
