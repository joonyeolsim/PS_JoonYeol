import sys

if __name__ == '__main__':
    n = int(input())
    input_sequence = []
    sequence_stack = []
    output_stack = []

    for i in range(n):
        input_sequence.append(int(sys.stdin.readline().rstrip()))

    last_num = 0
    cnt = 1

    for cur_num in input_sequence:
        if cur_num > last_num:

            # push
            while cnt <= cur_num:
                sequence_stack.append(cnt)
                output_stack.append('+')
                cnt += 1
            sequence_stack.pop()
            output_stack.append('-')

        else:
            if sequence_stack.pop() != cur_num:
                output_stack = ['NO']
                break
            else:
                output_stack.append('-')

        last_num = cur_num

    # output 출력
    for output in output_stack:
        print(output)
