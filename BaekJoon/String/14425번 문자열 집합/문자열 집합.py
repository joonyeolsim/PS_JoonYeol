import sys

if __name__ == '__main__':
    N, M = map(int, input().split())

    string_union = []
    result = 0

    for _ in range(N):
        string_union.append(sys.stdin.readline().rstrip())

    for _ in range(M):
        input_str = sys.stdin.readline().rstrip()
        if input_str in string_union:
            result += 1

    print(result)