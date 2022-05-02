def num_transpose(n, k):
    result = 0
    count = 0
    while n:
        result += n % k * 10 ** count
        n = n // k
        count += 1
    return str(result)


def is_prime(num):
    if num == 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            break
        i += 1
    else:
        return True
    return False


def solution(n, k):
    answer = 0
    transposed_num = num_transpose(n, k)

    next_num = ""
    transposed_num += "0"
    for num in transposed_num:
        if num != "0":
            next_num += num
        else:
            if next_num and is_prime(int(next_num)):
                answer += 1
            next_num = ""

    return answer


if __name__ == '__main__':
    print(solution(110011, 10))