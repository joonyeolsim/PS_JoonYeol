import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    cow_dict = dict()
    move = 0
    for _ in range(N):
        cow, location = map(int, sys.stdin.readline().split())
        if cow in cow_dict.keys():
            if location != cow_dict[cow]:
                move += 1
                cow_dict[cow] = location
        else:
            cow_dict[cow] = location
    print(move)
