if __name__ == '__main__':
    N = int(input())
    pc_list = [0 for _ in range(101)]
    count = 0
    customers = list(map(int, input().split()))
    for customer in customers:
        if customer <= 100 and not pc_list[customer]:
            pc_list[customer] = 1
        else:
            count += 1
    print(count)
