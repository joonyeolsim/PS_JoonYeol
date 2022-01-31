if __name__ == '__main__':
    cnt = int(input())
    grade_list = list(map(int, input().split()))
    max_grade = max(grade_list)
    result = 0
    for i, grade in enumerate(grade_list):
        result += grade / max_grade * 100
    print(result/len(grade_list))
