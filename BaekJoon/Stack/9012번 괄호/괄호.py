if __name__ == '__main__':
    cnt = int(input())
    result_list = []
    for _ in range(cnt):
        bracket_stack = []
        for bracket in input():
            bracket_stack.append(bracket)
            if len(bracket_stack) > 1 and bracket_stack[-2:] == ['(', ')']:
                bracket_stack = bracket_stack[:-2]
        if bracket_stack:
            result_list.append('NO')
        else:
            result_list.append('YES')

    print(*result_list, sep='\n')
