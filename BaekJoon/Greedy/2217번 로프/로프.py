import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    rope_list = []
    max_weight = 0

    for _ in range(N):
        rope_list.append(int(sys.stdin.readline()))

    rope_list.sort(reverse=True)
    for k in range(1, N+1):
        weight = rope_list[k - 1] * k
        if weight > max_weight:
            max_weight = weight
    print(max_weight)