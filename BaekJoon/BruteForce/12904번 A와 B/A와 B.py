def recursive_func(s, t):
    # 기저 사례 1: s가 t보다 길다면 False
    if len(s) > len(t):
        return False

    # 기저 사례 2: s와 t가 같다면 True
    if s == t:
        return True

    if t[-1] == "A":
        t = t[:-1]

    elif t[-1] == "B":
        t = t[:-1]
        t = t[::-1]

    return recursive_func(s, t)


if __name__ == '__main__':
    S = input()
    T = input()
    if recursive_func(S, T):
        print(1)
    else:
        print(0)
