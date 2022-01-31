import math

if __name__ == '__main__':
    D, H, W = map(int, input().split())

    L = math.sqrt(H**2 + W**2)
    ratio = D / L
    real_h = int(H * ratio)
    real_w = int(W * ratio)

    print(real_h, real_w)