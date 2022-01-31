from string import ascii_lowercase

if __name__ == '__main__':
    sentence = input()
    alphabet_list = list(ascii_lowercase)
    for alphabet in alphabet_list:
        try:
            print(sentence.index(alphabet), end=' ')
        except ValueError:
            print('-1', end=' ')
