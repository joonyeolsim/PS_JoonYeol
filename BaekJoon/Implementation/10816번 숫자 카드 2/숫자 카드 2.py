import sys

N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().strip())
find_nums = list(map(int, sys.stdin.readline().split()))

num_dict = dict()
for num in nums:
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1

for find_num in find_nums:
    if find_num in num_dict:
        print(num_dict[find_num])
    else:
        print(0)
