if __name__ == '__main__':
    N = int(input())
    max_num = 0
    for i in range(N + 1):
        flag = True
        temp = str(i)
        for num in temp:
            if num != '4' and num != '7':
                flag = False
                break
        if flag:
            max_num = i
    print(max_num)