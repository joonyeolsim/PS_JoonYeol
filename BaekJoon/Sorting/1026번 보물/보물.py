if __name__ == '__main__':
    N = int(input())

    num1 = list(map(int, input().split()))
    num2 = list(map(int, input().split()))

    num1.sort()
    num2.sort(reverse=True)

    S = 0
    for i in range(N):
        S += num1[i] * num2[i]

    print(S)