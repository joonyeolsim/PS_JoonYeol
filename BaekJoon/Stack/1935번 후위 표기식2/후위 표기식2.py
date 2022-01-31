from string import ascii_uppercase

if __name__ == '__main__':
    n = int(input())
    expression = list(input())
    alpha_list = list(ascii_uppercase)
    for i in range(n):
        change_value = input()
        for j, ch in enumerate(expression):
            if ch == alpha_list[i]:
                expression[j] = change_value

    stack = []
    for factor in expression:
        if factor == '+':
            stack.append(stack.pop() + stack.pop())
        elif factor == '-':
            stack.append(-(stack.pop() - stack.pop()))
        elif factor == '*':
            stack.append(stack.pop() * stack.pop())
        elif factor == '/':
            num = stack.pop()
            stack.append(stack.pop() / num)
        else:
            stack.append(int(factor))
    print('{:.2f}'.format(stack.pop()))
