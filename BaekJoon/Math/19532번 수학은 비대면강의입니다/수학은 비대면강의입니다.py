import sys

if __name__ == '__main__':
    num_list = list(map(int, sys.stdin.readline().split()))

    value = []

    for i in range(-999, 1000):
        for j in range(-999, 1000):
            if num_list[0] * i + num_list[1] * j == num_list[2]:
                value.append([i, j])

    for xy in value:
        if num_list[3] * xy[0] + num_list[4] * xy[1] == num_list[5]:
            print(xy[0], xy[1])
            break