# 유클리드 호제법
def get_gcd_lcm(a, b):
    multiply_ab = a * b
    while b > 0:
        a, b = b, a % b
    return a, multiply_ab // a


if __name__ == '__main__':
    a, b = map(int, input().split())
    gcd, lcm = get_gcd_lcm(a, b)
    print(gcd)
    print(lcm)
