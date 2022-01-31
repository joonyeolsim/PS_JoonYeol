if __name__ == '__main__':
    count = 0
    num_list = []
    while count < 1000:
        count += 1
        for i in range(count):
            num_list.append(count)
    num_input = list(map(int, input().split()))
    print(sum(num_list[num_input[0] - 1:num_input[1]]))
