if __name__ == '__main__':
    static_price, dynamic_price, notebook_price = map(int, input().split())

    if dynamic_price >= notebook_price:
        print(-1)
    else:
        result = static_price // (notebook_price - dynamic_price) + 1
        print(result)