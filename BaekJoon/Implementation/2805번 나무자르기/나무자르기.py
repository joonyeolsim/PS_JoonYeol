import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    woods = list(map(int, sys.stdin.readline().split()))
    max_height = max(woods)
    min_height = 0
    mid_height = (max_height + min_height) // 2

    while min_height <= max_height:
        wood_sum = 0
        for wood in woods:
            wood_value = wood - mid_height
            if wood_value > 0:
                wood_sum += wood_value

        if wood_sum == M or mid_height == min_height or mid_height == max_height :
            break

        elif wood_sum > M:
            min_height = mid_height

        elif wood_sum < M:
            max_height = mid_height

        mid_height = (min_height + max_height) // 2

    print(mid_height)