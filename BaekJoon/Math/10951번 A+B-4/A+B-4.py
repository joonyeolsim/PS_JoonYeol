import sys

if __name__ == '__main__':
    while True:
        try:
            a, b = map(int, sys.stdin.readline().rstrip().split())
        except ValueError:
            break
        print(a + b)
