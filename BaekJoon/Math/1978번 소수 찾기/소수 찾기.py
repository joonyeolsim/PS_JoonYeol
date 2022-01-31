def is_prime(number):
    if number == 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    cnt = int(input())
    num_list = map(int, input().split())
    result = 0

    for num in num_list:
        if is_prime(num):
            result += 1
    print(result)
