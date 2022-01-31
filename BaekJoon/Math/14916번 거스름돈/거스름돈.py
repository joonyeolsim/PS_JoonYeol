if __name__ == '__main__':
    n = int(input())
    cnt = 0
    while n > 0:
        if n >= 5 and ((n - 5) % 5 == 0 or (n - 5) % 2 == 0):
            n -= 5
            cnt += 1
        elif n >= 2 and ((n - 2) % 5 == 0 or (n - 2) % 2 == 0):
            n -= 2
            cnt += 1
        else:
            cnt = 0
            break
    if cnt:
        print(cnt)
    else:
        print(-1)
