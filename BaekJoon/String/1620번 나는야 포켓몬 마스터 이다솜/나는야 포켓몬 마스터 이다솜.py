import sys

if __name__ == '__main__':
    N, M = map(int, input().split())
    pokemon_dict = dict()

    for i in range(N):
        pokemon_name = sys.stdin.readline().rstrip()
        pokemon_dict[i+1] = pokemon_name
        pokemon_dict[pokemon_name] = i+1

    for _ in range(M):
        query = sys.stdin.readline().rstrip()
        if query.isdigit():
            print(pokemon_dict[int(query)])
        else:
            print(pokemon_dict[query])
