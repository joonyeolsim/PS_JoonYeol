import sys

N = int(sys.stdin.readline().strip())
nums = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
find_nums = list(map(int, sys.stdin.readline().split()))

for find_num in find_nums:
    if find_num in nums:
        print(1)
    else:
        print(0)
