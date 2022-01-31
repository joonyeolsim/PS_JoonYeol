if __name__ == '__main__':
    croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    sentence = input()
    result = 0
    for ch in croatia:
        if ch in sentence:
            sentence = sentence.replace(ch, "0")
            result += 1

    result += len(sentence) - result
    print(result)
