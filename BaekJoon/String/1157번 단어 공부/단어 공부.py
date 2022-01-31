if __name__ == '__main__':
    sentence = input().lower()
    max_ch = ""
    max_value = 0
    second_max_value = 0
    use_list = []

    for ch in sentence:
        if ch in use_list:
            continue
        cnt = sentence.count(ch)
        if max_value < cnt:
            max_value = cnt
            max_ch = ch
        elif max_value == cnt:
            second_max_value = cnt
        use_list.append(ch)

    if max_value > second_max_value:
        print(max_ch.upper())
    else:
        print("?")