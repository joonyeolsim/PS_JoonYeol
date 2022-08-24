import sys

num = sys.stdin.readline().strip()

while num != "0":
    if num == num[::-1]:
        print("yes")
    else:
        print("no")

    num = sys.stdin.readline().strip()