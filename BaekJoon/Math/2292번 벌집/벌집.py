if __name__ == '__main__':
    approach = int(input())
    bound = 1
    pre_bound = 0
    cnt = 1

    while True:
        if pre_bound < approach <= bound:
            break
        pre_bound = bound
        bound = bound + 6 * cnt
        cnt += 1
    print(cnt)