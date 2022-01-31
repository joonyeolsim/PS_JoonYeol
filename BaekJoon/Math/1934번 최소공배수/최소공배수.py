if __name__ == '__main__':
    cnt = int(input())
    result_list = []

    for i in range(cnt):
        a, b = map(int, input().split())
        multiply_ab = a * b
        while b > 0:
            a, b = b, a % b
        result_list.append(multiply_ab // a)

    for result in result_list:
        print(result)
