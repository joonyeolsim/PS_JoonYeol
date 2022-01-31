if __name__ == '__main__':
    T = int(input())
    threshold = 4
    for i in range(1, T+1):
        for j in range(T, 0, -1):
            if i < j:
                print(' ', end='')
            else:
                print('*', end='')
        print('', end='\n')
