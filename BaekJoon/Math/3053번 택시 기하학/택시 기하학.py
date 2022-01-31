import math

if __name__ == '__main__':
    R = int(input())

    # 유클리드 기하학
    print("{0:.6f}".format(math.pi * R ** 2))

    # 택시 기하학
    print("{0:.6f}".format(2 * R ** 2))