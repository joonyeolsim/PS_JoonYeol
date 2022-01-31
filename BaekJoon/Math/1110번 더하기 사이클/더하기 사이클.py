if __name__ == '__main__':
    num = int(input())
    original_num = num
    cnt = 0

    units = num % 10
    tens = (num // 10)
    num = units * 10 + (units + tens) % 10
    cnt += 1
    while num != original_num:
        units = num % 10
        tens = (num // 10)
        num = units * 10 + (units + tens) % 10
        cnt += 1
    print(cnt)


