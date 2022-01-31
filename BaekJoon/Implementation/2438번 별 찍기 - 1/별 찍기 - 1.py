if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        for j in range(i+1):
            print('*', end='')
        print('', end='\n')
