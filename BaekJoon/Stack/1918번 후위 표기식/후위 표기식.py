operator = ['+', '-', '*', '/']


# 괄호 생성기
def make_parentheses(expression):
    factor_stack = []
    recursive_factor = ""
    recursive_semaphore = 0
    new_flag = False

    # 곱하기, 나누기 묶어주기
    for factor in expression:
        if factor == '(':
            recursive_semaphore += 1
        elif factor == ')':
            recursive_semaphore -= 1

        if recursive_semaphore > 0:
            recursive_factor += factor

        else:
            if recursive_factor:
                factor = make_parentheses(recursive_factor[1:])
                recursive_factor = ""

            factor_stack.append(factor)

            if new_flag:
                second = factor_stack.pop()
                cur_operator = factor_stack.pop()
                first = factor_stack.pop()
                parentheses_expression = '(' + first + cur_operator + second + ')'
                factor_stack.append(parentheses_expression)
                new_flag = False
            if factor in operator[2:]:
                new_flag = True

    # 더하기, 빼기 묶어주기
    while len(factor_stack) > 1:
        parentheses_expression = '(' + factor_stack.pop(0) + factor_stack.pop(0) + factor_stack.pop(0) + ')'
        factor_stack.insert(0, parentheses_expression)

    return factor_stack[0]


# 후위 표기식 변환 함수 -> 재귀로 구현
def change_to_postfix_notation(expression):
    first_factor = ""
    cur_operator = ""
    second_factor = ""

    # 괄호 제거
    expression = expression[1:-1]

    flag = 0

    for i, ch in enumerate(expression):
        if ch == '(':
            flag += 1
        if ch in operator:
            if flag:
                flag -= 1
            else:
                first_factor = expression[:i]
                cur_operator = expression[i]
                second_factor = expression[i + 1:]
                break

    if '(' in first_factor:
        first_factor = change_to_postfix_notation(first_factor)

    if '(' in second_factor:
        second_factor = change_to_postfix_notation(second_factor)

    return first_factor + second_factor + cur_operator


if __name__ == '__main__':
    text = input()
    if len(text) == 1:
        result = text
    else:
        text = make_parentheses(text)
        result = change_to_postfix_notation(text)
    print(result)

