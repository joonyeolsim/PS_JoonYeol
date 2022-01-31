import sys


def get_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, sys.stdin.readline().split()))
    X = int(input())

    disjoint = []
    for a in A:
        if get_gcd(a, X) == 1:
            disjoint.append(a)
    print(sum(disjoint) / len(disjoint))

