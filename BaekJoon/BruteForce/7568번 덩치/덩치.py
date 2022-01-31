import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    info_list = []

    for i in range(N):
        w, h = map(int, sys.stdin.readline().split())
        rank = 1
        for info in info_list:
            if info[0] > w and info[1] > h:
                rank += 1
            elif info[0] < w and info[1] < h:
                info[2] += 1
        info_list.append([w, h, rank])

    for info in info_list:
        print(info[2], end=' ')
