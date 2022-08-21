import sys


def is_finish(cube_):
    j = 1
    count = 0
    while j < 24:
        if cube_[j] == cube_[j + 1] == cube_[j + 2] == cube_[j + 3]:
            count += 1
        j += 4
    if count == 6:
        return True
    return False


squares = [[13, 14, 5, 6, 17, 18, 21, 22],
           [15, 16, 7, 8, 19, 20, 23, 24],
           [1, 3, 5, 7, 9, 11, 24, 22],
           [2, 4, 6, 8, 10, 12, 23, 21],
           [3, 4, 17, 19, 10, 9, 16, 14],
           [1, 2, 18, 20, 12, 11, 15, 13]]

result = 0
cube = [0] + list(map(int, sys.stdin.readline().split()))

for s in squares:
    copy_cube = cube[:]
    color1 = copy_cube[s[6]]
    color2 = copy_cube[s[7]]
    for i in range(6, 1, -2):
        copy_cube[s[i]] = copy_cube[s[i - 2]]
        copy_cube[s[i + 1]] = copy_cube[s[i - 1]]

    copy_cube[s[0]] = color1
    copy_cube[s[1]] = color2
    if is_finish(copy_cube):
        result = 1

    copy_cube = cube[:]
    color1 = copy_cube[s[0]]
    color2 = copy_cube[s[1]]
    for i in range(2, 7, 2):
        copy_cube[s[i - 2]] = copy_cube[s[i]]
        copy_cube[s[i - 1]] = copy_cube[s[i + 1]]

    copy_cube[s[6]] = color1
    copy_cube[s[7]] = color2

    if is_finish(copy_cube):
        result = 1

print(result)