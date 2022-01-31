if __name__ == '__main__':
    N, B = input().split()
    result = 0
    B = int(B)
    L = len(N)
    for i, n in enumerate(N):
        result += B ** (L - i - 1) * (ord(n) - 55) if n.isalpha() else B ** (L - i - 1) * int(n)

    print(result)