import sys

if __name__ == '__main__':
    M, N = map(int, sys.stdin.readline().split())

    universe_list = []
    count = 0

    for i in range(M):
        planets = list(map(int, sys.stdin.readline().split()))
        planet_matrix = [[0] * N for _ in range(N)]
        for j in range(len(planets)):
            for k in range(j + 1, len(planets)):
                if planets[j] < planets[k]:
                    planet_matrix[j][k] = 1
                elif planets[j] == planets[k]:
                    planet_matrix[j][k] = 2
                elif planets[j] > planets[k]:
                    planet_matrix[j][k] = 3
        universe_list.append(planet_matrix)
        for universe in universe_list[:-1]:
            if universe == universe_list[-1]:
                count += 1

    print(count)