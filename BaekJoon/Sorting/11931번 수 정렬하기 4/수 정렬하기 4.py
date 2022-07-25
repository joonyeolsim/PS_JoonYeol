import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    nums = []

    for _ in range(N):
        nums.append(int(sys.stdin.readline().strip()))

    nums.sort(reverse=True)
    for n in nums:
        print(n)
