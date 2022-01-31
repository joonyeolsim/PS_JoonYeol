def logic(compare, num, _stack):
    tmp = 0
    while isinstance(stack[-1], int):
        tmp += _stack.pop()

    if tmp != 0:
        _stack.pop()
        _stack.append(tmp * num)

    if _stack[-1] == compare:
        _stack.pop()
        _stack.append(num)


if __name__ == '__main__':
    stack = []
    bracket_stack = []

    N = input()
    for n in N:
        if n == ')':
            if bracket_stack and bracket_stack[-1] == '(':
                bracket_stack.pop()
                logic('(', 2, stack)
            else:
                print(0)
                exit(0)

        elif n == ']':
            if bracket_stack and bracket_stack[-1] == '[':
                bracket_stack.pop()
                logic('[', 3, stack)
            else:
                print(0)
                exit(0)

        else:
            bracket_stack.append(n)
            stack.append(n)

    if not bracket_stack:
        print(sum(stack))
    else:
        print(0)