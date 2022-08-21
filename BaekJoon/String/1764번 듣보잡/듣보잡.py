import sys

name_dict = dict()
N, M = map(int, sys.stdin.readline().split())

for _ in range(N):
    name = sys.stdin.readline().strip()
    if name not in name_dict:
        name_dict[name] = 1
    else:
        name_dict[name] += 1

for _ in range(M):
    name = sys.stdin.readline().strip()
    if name not in name_dict:
        name_dict[name] = 1
    else:
        name_dict[name] += 1

count = 0
name_list = []
for name in name_dict.keys():
    if name_dict[name] == 2:
        count += 1
        name_list.append(name)

print(count)
print(*sorted(name_list), sep="\n")