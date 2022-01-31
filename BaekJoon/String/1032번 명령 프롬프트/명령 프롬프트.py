import sys

if __name__ == '__main__':
    N = int(input())
    text_list = []
    result = ""
    flag = False

    for _ in range(N):
        text_list.append(sys.stdin.readline().rstrip())

    for i, ch in enumerate(text_list[0]):
        for text in text_list[1:]:
            if ch != text[i]:
                flag = True
                break
        if flag:
            result += '?'
            flag = False
        else:
            result += ch

    print(result)