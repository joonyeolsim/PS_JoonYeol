self_num_list = [i for i in range(1, 10000)]
not_self_num_list = []


def create_self_num(num):
    # create self_num
    self_num = num
    self_num += sum(map(int, str(self_num)))

    if self_num >= 10000:
        return self_num

    if self_num not in self_num_list:
        return self_num

    if self_num in self_num_list:
        self_num_list.pop(self_num_list.index(self_num))

    create_self_num(self_num)


if __name__ == '__main__':
    i = 0
    while len(self_num_list) > i:
        create_self_num(self_num_list[i])
        print(self_num_list[i])
        i += 1
