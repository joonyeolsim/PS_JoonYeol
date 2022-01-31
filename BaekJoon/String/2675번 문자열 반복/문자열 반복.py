if __name__ == '__main__':
    cnt = int(input())
    for i in range(cnt):
        num, sentence = input().split()
        for ch in sentence:
            for j in range(int(num)):
                print(ch, end='')
        print(end='\n')


