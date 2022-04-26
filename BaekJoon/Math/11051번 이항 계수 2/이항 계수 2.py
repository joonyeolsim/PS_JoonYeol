import math


if __name__ == '__main__':
    n, k = map(int, input().split())
    print((math.factorial(n) // (math.factorial(k) * math.factorial(n - k))) % 10007)