import math

if __name__ == '__main__':
    n = int(input())
    fact = str(math.factorial(n))
    for i in fact[::-1]:
        if i == '0':
            continue
            
        else:
            print(i)
            break
