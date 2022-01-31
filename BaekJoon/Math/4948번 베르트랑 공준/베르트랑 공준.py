import sys
import math

def is_prime(num):
    for k in range(2, int(math.sqrt(num)) + 1):
        if num % k == 0:
            return False
    return True


if __name__ == '__main__':
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            break

        cnt = 0
        for i in range(n+1, 2*n+1):
            if is_prime(i):
                cnt += 1
        print(cnt)
