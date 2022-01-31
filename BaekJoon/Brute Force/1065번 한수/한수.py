def is_hansu(num):
    unit_list = list(map(int, str(num)))
    if len(unit_list) > 1:
        init_cd = unit_list[1] - unit_list[0]
        for j in range(len(unit_list) - 1):
            cd = unit_list[j+1] - unit_list[j]
            if cd != init_cd:
                return False
    else:
        return True
    return True


if __name__ == '__main__':
    num = int(input())
    result = 0
    for i in range(num):
        if is_hansu(i+1):
            result += 1
    print(result)

