if __name__ == '__main__':
    remain_list = []
    result = 0
    for i in range(10):
        remain = int(input()) % 42
        if remain not in remain_list:
            remain_list.append(remain)
            result += 1
    print(result)