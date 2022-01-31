import re

if __name__ == '__main__':
    polynomial = input()
    result = ''
    linear_term = re.findall('-?\d+x', polynomial)
    constant = re.findall('[-, +]?\d+$', polynomial)

    if polynomial == '0':
        result = 'W'
    else:
        if linear_term:
            num = str(int(linear_term[0][:-1]) // 2)
            if num[0].isdigit() or num[0] == '+':
                sign = ''
            else:
                sign = '-'

            if num in ['1', '-1']:
                result += sign + 'xx'
            else:
                result += num + 'xx'

        if constant:
            num = constant[0]
            if num not in ['+0', '-0']:
                if num[0].isdigit() or num[0] == '+':
                    sign = '+'
                else:
                    sign = '-'

                if num == '1':
                    result += 'x'
                elif num in ['-1', '+1']:
                    result += sign + 'x'
                else:
                    result += num + 'x'

        result += '+W'

    print(result)