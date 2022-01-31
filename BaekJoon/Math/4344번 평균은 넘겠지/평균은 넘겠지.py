if __name__ == '__main__':
    case_num = int(input())
    for i in range(case_num):
        grades = list(map(int, input().split()))
        student_num = grades.pop(0)
        avg = sum(grades) / len(grades)
        high_student_num = 0
        for grade in grades:
            if grade > avg:
                high_student_num += 1
        result = format((high_student_num / student_num) * 100, ".3f")
        print(result + "%")
