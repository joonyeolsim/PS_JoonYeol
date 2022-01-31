import math

if __name__ == '__main__':
    a, b, v = map(int, input().split())
    last_value = v - a
    result = math.ceil(last_value / (a - b)) + 1
    print(result)
