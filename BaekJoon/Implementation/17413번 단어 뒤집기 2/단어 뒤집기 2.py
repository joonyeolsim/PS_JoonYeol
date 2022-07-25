if __name__ == '__main__':
    stack = []

    sentence = input()
    flag = False
    temp = ""

    for ch in sentence:
        if ch == '<':
            if temp:
                stack.append(temp[::-1])
                temp = ""
            temp += ch
            flag = True

        elif ch == '>':
            temp += ch
            flag = False
            stack.append(temp)
            temp = ""

        elif ch == " " and not flag:
            temp += ch
            temp = temp[:-1]
            stack.append(temp[::-1] + " ")
            temp = ""
        else:
            temp += ch

    if temp:
        stack.append(temp[::-1])

    for s in stack:
        print(s, end="")