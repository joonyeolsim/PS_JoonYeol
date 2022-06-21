import sys

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        n = int(sys.stdin.readline().strip())
        binary_array = []
        while n > 0:
            binary_array.append(n % 2)
            n //= 2

        for i, binary in enumerate(binary_array):
            if binary:
                print(i, end=' ')
        print()
