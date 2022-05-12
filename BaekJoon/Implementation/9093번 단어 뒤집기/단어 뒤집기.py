if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        word_list = list(input().split())
        for word in word_list:
            print(word[::-1], end=' ')