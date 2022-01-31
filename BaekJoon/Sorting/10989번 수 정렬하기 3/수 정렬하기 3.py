import sys

if __name__ == '__main__':
    cnt = int(sys.stdin.readline().rstrip())
    num_list = [0] * 10001
    for _ in range(cnt):
        num_list[int(sys.stdin.readline().rstrip())] += 1

    this_num = 0
    for num in num_list:
        for _ in range(num):
            print(this_num)
        this_num += 1