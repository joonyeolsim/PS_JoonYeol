if __name__ == '__main__':
    N = int(input())
    result = []
    people = []

    for i in range(N):
        k = int(input())
        n = int(input())

        for j in range(1, k * n + n + 1):
            now = 0
            left = j - 1
            down = j - n

            if down > 0:
                now += people[down - 1]
            else:
                now += 1

            if j % n != 1 and n != 1:
                now += people[left - 1]

            people.append(now)
        result.append(people.pop())
        people.clear()

    print(*result, sep='\n')
