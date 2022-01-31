import sys

if __name__ == '__main__':
    K = int(sys.stdin.readline().rstrip())
    num_list = []
    for _ in range(K):
        n = int(sys.stdin.readline().rstrip())
        if n != 0:
            num_list.append(n)
        else:
            num_list.pop()
    print(sum(num_list))