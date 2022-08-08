import sys

if __name__ == '__main__':
    M, N = map(int, input().split())
    universe_list = []

    for _ in range(M):
        u_input = dict((x, True) for x in map(int, sys.stdin.readline().split())).keys()
        universe = {i: u for i, u in enumerate(u_input)}
        universe = sorted(universe, key=universe.get)
        universe_list.append(tuple(universe))

    count = 0
    for i in range(len(universe_list)):
        for j in range(i + 1, len(universe_list)):
            if universe_list[i] == universe_list[j]:
                count += 1

    print(count)