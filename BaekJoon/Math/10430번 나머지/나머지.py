if __name__ == '__main__':
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    print((a + b) % c)
    print(((a % c) + (b % c)) % c)
    print((a * b) % c)
    print(((a % c) * (b % c)) % c)
