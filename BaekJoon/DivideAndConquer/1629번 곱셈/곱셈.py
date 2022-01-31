import sys

if __name__ == '__main__':
    a, b, mod = map(int, sys.stdin.readline().split())
    bin_b = int(format(b, 'b'))
    index = 0

    # base case
    mod_b = [a % mod]
    temp_b = bin_b // 10

    # common case
    while temp_b > 0:
        mod_b.append((mod_b[index] ** 2) % mod)
        temp_b = temp_b // 10
        index += 1

    index = 0
    result = 1
    while bin_b > 0:
        val = bin_b % 10
        bin_b = bin_b // 10

        if val:
            result *= mod_b[index]
        index += 1

    print(result % mod)