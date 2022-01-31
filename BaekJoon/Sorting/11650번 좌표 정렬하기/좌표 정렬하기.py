import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    coordinate_list = []

    for _ in range(N):
        coordinate_list.append(tuple(map(int,sys.stdin.readline().split())))

    coordinate_list.sort()
    for coordinate in coordinate_list:
        print(*coordinate, sep=' ')
