if __name__ == '__main__':
    cnt = int(input())

    a_list = []
    for i in range(cnt):
        a = int(input())
        a_list.append(a)

    a_list.sort()

    for index in range(len(a_list) - 1):
        print(a_list[index])
    print(a_list[cnt - 1], end='')