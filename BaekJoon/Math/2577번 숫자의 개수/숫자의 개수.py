if __name__ == '__main__':
    unit_list = [0 for i in range(10)]
    a = int(input())
    b = int(input())
    c = int(input())
    new_num = a * b * c
    for i in range(len(str(new_num))):
        unit_list[new_num % 10] += 1
        new_num = new_num // 10

    for unit in unit_list:
        print(unit)