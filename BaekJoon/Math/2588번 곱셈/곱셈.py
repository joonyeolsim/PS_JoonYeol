if __name__ == '__main__':
    n = 3
    remainder = 0
    num1 = int(input())
    num2 = int(input())
    result = 0

    for i in range(n):
        remainder = num2 % 10
        print(num1 * remainder)
        result += (num1 * remainder) * 10 ** i
        num2 = num2 // 10

    print(result)