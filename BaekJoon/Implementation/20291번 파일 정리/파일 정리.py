import sys

if __name__ == '__main__':
    cnt = int(sys.stdin.readline().strip())
    extension_cnt = {}

    for _ in range(cnt):
        filename = sys.stdin.readline().strip()
        _, extension = filename.split('.')
        if extension not in extension_cnt.keys():
            extension_cnt[extension] = 1
        else:
            extension_cnt[extension] += 1

    for key in sorted(extension_cnt.keys()):
        print(key + " " + str(extension_cnt[key]))