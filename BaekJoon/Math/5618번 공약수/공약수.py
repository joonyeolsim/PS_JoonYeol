import sys


def get_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    n = int(sys.stdin.readline())

    num_list = list(map(int, sys.stdin.readline().rstrip().split()))
    while len(num_list) > 1:
        num_list.append(get_gcd(num_list.pop(), num_list.pop()))

    gcd = num_list.pop()
    for i in range(1, gcd // 2 + 1):
        if gcd % i == 0:
            print(i)
    print(gcd)

