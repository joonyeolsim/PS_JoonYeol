import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    n_list = []
    for _ in range(T):
        N = int(sys.stdin.readline().strip())
        n_list = list(map(int, sys.stdin.readline().split()))

        print(str(min(n_list)) + ' ' + str(max(n_list)))