if __name__ == '__main__':
    a_list = list(map(int, input().split()))

    pre_a = a_list[0]
    total_sum = 0

    for a in a_list[1:]:
        total_sum += pre_a - a
        pre_a = a
    if total_sum == 7:
        print("descending")
    elif total_sum == -7:
        print("ascending")
    else:
        print("mixed")
