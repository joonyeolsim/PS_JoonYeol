import sys

# 유클리드 호제법
def get_gcd_lcm(a, b):
    multiply_ab = a * b
    while b > 0:
        a, b = b, a % b
    return a, multiply_ab // a


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())

    for _ in range(N):
        n, m = map(int, sys.stdin.readline().split())
        dummy, lcm = get_gcd_lcm(n, m)
        print(lcm)

