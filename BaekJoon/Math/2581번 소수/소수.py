import math


def is_prime(prime_num):
    for i in range(2, int(math.sqrt(prime_num))+1):
        if prime_num % i == 0:
            return False
    return True


if __name__ == '__main__':
    a = int(input())
    b = int(input())

    minimum_prime = 0
    prime_sum = 0
    one_flag = True

    if a == 1:
        a = 2

    for num in range(a, b+1):
        if is_prime(num):
            prime_sum += num
            if one_flag:
                minimum_prime = num
                one_flag = False

    if prime_sum == 0:
        print(-1)
    else:
        print(prime_sum)
        print(minimum_prime, end='')
