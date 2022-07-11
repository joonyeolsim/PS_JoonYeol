if __name__ == '__main__':
    submit_student_list = [0 for _ in range(31)]

    for _ in range(28):
        student = int(input())
        submit_student_list[student] = 1

    for student_num, is_submit in enumerate(submit_student_list[1:]):
        if not is_submit:
            print(student_num + 1)