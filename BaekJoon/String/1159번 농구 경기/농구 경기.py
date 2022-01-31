import sys

if __name__ == '__main__':
    N = int(input())
    name_dict = {}
    result = []

    for _ in range(N):
        name = sys.stdin.readline().rstrip()[0]
        if not name in name_dict.keys():
            name_dict[name] = 1
        else:
            name_dict[name] += 1
            if name_dict[name] == 5:
                result.append(name)

    if result:
        result.sort()
        print(''.join(result))
    else:
        print("PREDAJA")
