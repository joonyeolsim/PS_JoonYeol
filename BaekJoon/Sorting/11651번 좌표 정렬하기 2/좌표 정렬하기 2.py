import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    coordinate_list = []

    for _ in range(N):
        coordinate_list.append(list(map(int, sys.stdin.readline().split()))[::-1])

    coordinate_list.sort()
    for coordinate in coordinate_list:
        print(str(coordinate[1]) + ' ' + str(coordinate[0]))
