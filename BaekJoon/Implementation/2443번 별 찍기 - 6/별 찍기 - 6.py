if __name__ == '__main__':
    num = int(input())

    for i in range(num):
        for _ in range(i):
            print(' ', end='')
        for _ in range((num - i) * 2 - 1):
            print('*', end='')
        print()
