if __name__ == '__main__':
    cnt = int(input())
    results = []

    for _ in range(cnt):
        num_list = []
        num_list += map(int, input().split())
        num_list.sort()
        results.append(num_list[-3])

    for result in results:
        print(result)