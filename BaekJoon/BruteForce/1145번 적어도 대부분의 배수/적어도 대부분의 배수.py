import math


def get_lcm(num1, num2):
    a = num1
    b = num2

    while b:
        a, b = b, a % b
    return (num1 * num2) // a


if __name__ == '__main__':
    num_list = list(map(int, input().split()))
    min_lcm = 100000000

    for i in range(5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                lcm = get_lcm(num_list[i], get_lcm(num_list[j], num_list[k]))
                min_lcm = lcm if lcm < min_lcm else min_lcm

    print(min_lcm)