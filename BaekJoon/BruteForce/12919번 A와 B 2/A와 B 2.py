def recursive_func(s, t):
    # 기저 사례 1: s가 t보다 길다면 False
    if len(s) > len(t):
        return False

    # 기저 사례 2: s와 t가 같다면 True
    if s == t:
        return True

    if t[-1] == "A":
        temp_t = t[:-1]
        if recursive_func(s, temp_t):
            return True

    temp_t = t[::-1]
    if temp_t[-1] == "B":
        temp_t = temp_t[:-1]
        if recursive_func(s, temp_t):
            return True


if __name__ == '__main__':
    S = input()
    T = input()
    if recursive_func(S, T):
        print(1)
    else:
        print(0)
