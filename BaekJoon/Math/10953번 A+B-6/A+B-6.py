import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())

    for _ in range(N):
        num1, num2 = map(int, sys.stdin.readline().split(','))
        print(num1 + num2)
