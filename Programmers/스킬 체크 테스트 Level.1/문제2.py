def solution(s):
    alphabet = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(10):
        s = s.replace(alphabet[i], str(i))
    answer = int(s)
    return answer


if __name__ == '__main__':
    print(solution("one4seveneight"))