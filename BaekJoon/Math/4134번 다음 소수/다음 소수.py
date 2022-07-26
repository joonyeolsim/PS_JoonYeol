import sys
import math


def is_prime(num):
    if num == 0 or num == 1:
        return False

    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False

    return True


if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        n = int(sys.stdin.readline().strip())
        while True:
            if is_prime(n):
                print(n)
                break
            n += 1
