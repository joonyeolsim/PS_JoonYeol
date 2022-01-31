# greedy algorithm
import sys
import math

if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        x, y = map(int, sys.stdin.readline().split())
        count = 0
        distance = y - x
        discriminator = math.isqrt(distance)
        # case 0
        if discriminator ** 2 == distance:
            print(discriminator * 2 - 1)

        # case 1
        if discriminator ** 2 < distance <= discriminator ** 2 + discriminator:
            print(discriminator * 2)
        # case 2
        elif discriminator ** 2 + discriminator < distance < (discriminator + 1) ** 2:
            print(discriminator * 2 + 1)
