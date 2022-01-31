import sys

if __name__ == '__main__':
    num1, num2 = map(list, sys.stdin.readline().split())
    num1_list = list(map(int, num1))
    num2_list = list(map(int, num2))
    print(sum(num1_list) * sum(num2_list))