if __name__ == '__main__':
    N, X = map(int, input().split())
    num = list(map(int, input().split()))
    for i in num:
        if i < X:
            print(str(i) + ' ', end='')


