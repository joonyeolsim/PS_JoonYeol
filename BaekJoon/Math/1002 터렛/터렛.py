import sys
import math

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
        d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

        if x1 == x2 and y1 == y2 and r1 == r2:
            print("-1")
        elif abs(r2 - r1) < d < r2 + r1:
            print("2")
        elif d == r2 + r1 or d == abs(r2 - r1):
            print("1")
        else:
            print("0")
