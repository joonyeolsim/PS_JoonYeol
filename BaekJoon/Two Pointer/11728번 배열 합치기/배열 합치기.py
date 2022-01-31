import sys

if __name__ == '__main__':
    N, M = sys.stdin.readline().split()
    s_list = list(map(int, sys.stdin.readline().split())) + list(map(int, sys.stdin.readline().split()))
    s_list.sort()
    print(*s_list, sep=' ')