if __name__ == '__main__':
    x_list = list()
    y_list = list()
    x_result = 0
    y_result = 0

    for _ in range(3):
        x, y = map(int, input().split())
        x_list.append(x)
        y_list.append(y)

    while x_list:
        x = x_list.pop(0)
        if x in x_list:
            x_list.remove(x)
        else:
            x_result = x

    while y_list:
        y = y_list.pop(0)
        if y in y_list:
            y_list.remove(y)
        else:
            y_result = y

    print(x_result, y_result)