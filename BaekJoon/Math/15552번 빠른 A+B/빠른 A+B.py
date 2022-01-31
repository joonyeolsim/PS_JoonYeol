import sys

if __name__ == '__main__':
    case_num = int(sys.stdin.readline().rstrip())

    for i in range(case_num):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        print(a + b)
