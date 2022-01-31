if __name__ == '__main__':
    x, y, w, h = map(int, input().split())
    x_to_zero = x
    y_to_zero = y
    x_to_w = w - x
    y_to_h = h - y
    print(min(x_to_zero, y_to_zero, x_to_w, y_to_h))