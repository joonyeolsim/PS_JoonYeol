if __name__ == '__main__':
    num = int(input())

    for i in range(num):
        for _ in range(num - i - 1):
            print(' ', end='')
        for _ in range(1 + 2 * i):
            print('*', end='')
        print()
