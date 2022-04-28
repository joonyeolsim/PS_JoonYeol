import math


def successive_squaring(a, s, p):
    square_list = [a]
    # 연속 제곱법
    bin_s = bin(s)[2:]
    bit_count = len(bin_s) - 1
    result = 1
    count = 0

    while bit_count > count:
        square_list.append(square_list[count] ** 2 % p)
        count += 1

    for i, b in enumerate(bin_s):
        if b == '1':
            result *= square_list[bit_count - i]
            result %= p

    return result


def factorial(n, p):
    result = 1

    while n > 1:
        result = result * n % p
        n -= 1

    return result


if __name__ == '__main__':
    n, k = map(int, input().split())
    p = 1000000007
    numer = factorial(n, p)
    denom_inverse = successive_squaring(factorial(k, p) * factorial(n - k, p), p - 2, p)
    print(numer * denom_inverse % p)