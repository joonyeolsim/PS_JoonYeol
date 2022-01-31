import math


# 에라토스체네스의 체
def get_factor(num):
    divisors = []

    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.append(i)
            divisors.append(num // i)

    divisors.sort()
    return divisors


# 유클리드 호제법
def get_gcd_lcm(a, b):
    multiply_ab = a * b
    while b > 0:
        a, b = b, a % b
    return a, multiply_ab // a


if __name__ == '__main__':
    a, b, L = map(int, input().split())
    if not(L % a or L % b):
        a_b_c_gcd = 0
        L_factors = get_factor(L)
        _, a_b_lcd = get_gcd_lcm(a, b)
        second_factor = L // a_b_lcd
        for L_factor in L_factors:
            a_b_c_gcd, _ = get_gcd_lcm(L // L_factor, second_factor)
            if a_b_c_gcd == 1:
                print(L_factor)
                break
    else:
        print(-1)
