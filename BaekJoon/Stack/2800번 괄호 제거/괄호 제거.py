if __name__ == '__main__':
    expression = input()
    stack = []
    index_stack = []
    for i, ch in enumerate(expression):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            stack.pop()
            

