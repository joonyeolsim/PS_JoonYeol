if __name__ == '__main__':
    ch_list = []
    previous_ch = ""
    result = 0
    cnt = int(input())

    for i in range(cnt):
        sentence = list(input())
        for ch in sentence:
            if previous_ch != ch:
                ch_list.append(previous_ch)
                if ch in ch_list:
                    result += 1
                    break
            previous_ch = ch
        previous_ch = ""
        ch_list.clear()

    print(cnt - result)