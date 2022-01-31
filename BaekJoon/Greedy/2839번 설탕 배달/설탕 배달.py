import math
from fractions import Fraction

if __name__ == '__main__':
    z = int(input())
    max_x = math.floor(z / 5)
    for x in range(max_x, -1, -1):
        f = Fraction(-2, 3) * x + Fraction(z, 3)
        if abs(int(f) - f) == 0:
            print(int(f))
            exit()
    print(-1)
