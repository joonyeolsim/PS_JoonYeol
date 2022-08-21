import sys

if __name__ == '__main__':
    pitch = sys.stdin.readline().strip()

    if pitch == "8 7 6 5 4 3 2 1":
        print("descending")
    elif pitch == "1 2 3 4 5 6 7 8":
        print("ascending")
    else:
        print("mixed")
