import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    info = list()
    for _ in range(N):
        age, name = sys.stdin.readline().split()
        info.append((int(age), name))
    info = sorted(info, key=lambda x: x[0])
    for i in info:
        print("{0} {1}".format(i[0], i[1]))