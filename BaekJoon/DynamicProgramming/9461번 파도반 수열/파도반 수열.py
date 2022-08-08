padovan_sequence = [1, 1, 1] + [0 for _ in range(97)]


def padovan(n):
    if n < 3:
        return padovan_sequence[n]

    if padovan_sequence[n]:
        return padovan_sequence[n]

    ret = padovan(n - 3) + padovan(n - 2)
    padovan_sequence[n] = ret
    return ret


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(padovan(N - 1))