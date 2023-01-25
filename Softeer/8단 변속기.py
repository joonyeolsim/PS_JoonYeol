import sys


if __name__ == '__main__':
    gears = list(map(int, sys.stdin.readline().split()))
    diffs = [gears[i] - gears[i - 1] for i in range(1, len(gears))]
    if diffs.count(1) == 7:
        print('ascending')
    elif diffs.count(-1) == 7:
        print('descending')
    else:
        print('mixed')