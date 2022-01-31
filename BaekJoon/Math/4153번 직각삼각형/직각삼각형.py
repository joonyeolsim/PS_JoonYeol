import sys

if __name__ == '__main__':
    while True:
        e1, e2, e3 = map(int, sys.stdin.readline().split())
        edge_list = [e1, e2, e3]
        edge_list.sort()
        if edge_list[0] == 0:
            break
        if edge_list[0] ** 2 + edge_list[1] ** 2 == edge_list[2] ** 2:
            print("right")
        else:
            print("wrong")