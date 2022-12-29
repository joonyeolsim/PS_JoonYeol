from itertools import combinations

if __name__ == '__main__':
    expression = input()
    result = set()
    index_stack = []
    stack = []
    for i, ch in enumerate(expression):
        if ch == '(':
            index_stack.append(i)
        elif ch == ')':
            stack.append((index_stack.pop(), i))

    for i in range(1, len(stack) + 1):
        for combination in list(combinations(stack, i)):
            temp_exp = list(expression[:])
            for first, second in combination:
                temp_exp[first] = ''
                temp_exp[second] = ''
            result.add(''.join(temp_exp))
    result = list(result)
    result.sort()
    print(*result, sep='\n')
