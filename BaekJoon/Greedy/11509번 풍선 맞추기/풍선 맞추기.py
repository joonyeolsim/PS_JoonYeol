import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
arrows = [0] * 1000001
count = 0

for i in range(n):
    if arrows[m[i]] == 0:
        count += 1
        arrows[m[i] - 1] += 1

    else:
        arrows[m[i]] -= 1
        arrows[m[i] - 1] += 1

print(count)