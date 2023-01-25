import sys


if __name__ == '__main__':
    M, N, K = map(int, sys.stdin.readline().split())
    secret_buttons = list(map(int, sys.stdin.readline().split()))
    user_buttons = list(map(int, sys.stdin.readline().split()))
    secret_flag = False

    for i in range(N - M + 1):
        count = 0
        for j in range(M):
            if user_buttons[i + j] == secret_buttons[j]:
                count += 1
            else:
                break
        if count == M:
            secret_flag = True
            break

    if secret_flag:
        print('secret')
    else:
        print('normal')