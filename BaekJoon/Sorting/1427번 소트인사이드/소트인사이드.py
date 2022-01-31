if __name__ == '__main__':
    str_num = input()
    num_list = []
    for ch in str_num:
        num_list.append(int(ch))

    num_list.sort(reverse=True)
    for num in num_list:
        print(num, end='')
