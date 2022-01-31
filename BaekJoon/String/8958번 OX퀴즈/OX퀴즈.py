if __name__ == '__main__':
    cnt = int(input())
    result = 0
    score = 0
    for i in range(cnt):
        case = input()
        for j in case:
            if j == 'O':
                score += 1
                result += score
            else:
                score = 0

        print(result)
        result = 0
        score = 0