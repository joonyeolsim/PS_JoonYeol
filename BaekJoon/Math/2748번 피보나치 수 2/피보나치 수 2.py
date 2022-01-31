if __name__ == '__main__':
    fibo_num = int(input())
    current, _next = 0, 1
    for _ in range(fibo_num):
        current, _next = _next, current + _next
    print(current)
