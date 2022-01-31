import sys


# 유클리드 호제법
def get_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    for _ in range(N):
        num_list = list(map(int, sys.stdin.readline().rstrip().split()))
        case = num_list.pop(0)
        if case > 1:
            result = 0
            for i in range(case):
                for j in range(i+1, case):
                    result += get_gcd(num_list[i], num_list[j])
            print(result)
        else:
            print(num_list.pop())
