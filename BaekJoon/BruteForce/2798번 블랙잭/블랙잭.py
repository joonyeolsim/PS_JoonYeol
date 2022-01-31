import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    num_list = list(map(int, sys.stdin.readline().split()))
    length = len(num_list)
    result = 0
    for i in range(length-2):
        for j in range(i+1, length-1):
            for k in range(j+1, length):
                num_sum = num_list[i] + num_list[j] + num_list[k]
                if M >= num_sum > result:
                    result = num_sum
    print(result)


