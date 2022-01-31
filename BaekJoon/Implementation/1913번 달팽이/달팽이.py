if __name__ == '__main__':
    snail_size = int(input())
    find_num = int(input())
    find_i = 0
    find_j = 0

    snail_array = [[0]*snail_size for _ in range(snail_size)]
    i = snail_size // 2
    j = snail_size // 2
    num = 0

    bound_start = snail_size // 2
    bound_limit = snail_size // 2

    flag = True

    for cnt in range(snail_size * snail_size):
        num += 1

        if flag:
            if i > bound_start:
                i = i - 1

            elif j < bound_limit:
                j = j + 1
                if j == bound_limit:
                    flag = False
        else:
            if i < bound_limit:
                i = i + 1

            elif j > bound_start:
                j = j - 1
                if j == bound_start:
                    flag = True
                    bound_start -= 1
                    bound_limit += 1

        snail_array[i][j] = num

        if num == (bound_limit - bound_start + 1) ** 2:
            bound_start -= 1
            bound_limit += 1

        if num == find_num:
            find_i = i + 1
            find_j = j + 1

    for small_array in snail_array:
        for factor in small_array:
            print(str(factor), end=' ')
        print('')
    print(str(find_i) + ' ' + str(find_j))