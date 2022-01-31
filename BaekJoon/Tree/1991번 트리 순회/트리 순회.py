def pre_order(node, _tree):
    print(node[0], end='')
    if node[1] != '.':
        for info in tree:
            if info[0] == node[1]:
                pre_order(info, _tree)
    if node[2] != '.':
        for info in tree:
            if info[0] == node[2]:
                pre_order(info, _tree)


def in_order(node, _tree):
    if node[1] != '.':
        for info in tree:
            if info[0] == node[1]:
                in_order(info, _tree)
    print(node[0], end='')
    if node[2] != '.':
        for info in tree:
            if info[0] == node[2]:
                in_order(info, _tree)


def post_order(node, _tree):
    if node[1] != '.':
        for info in tree:
            if info[0] == node[1]:
                post_order(info, _tree)
    if node[2] != '.':
        for info in tree:
            if info[0] == node[2]:
                post_order(info, _tree)
    print(node[0], end='')


if __name__ == '__main__':
    N = int(input())
    tree = []
    for _ in range(N):
        tree.append(list(input().split()))

    pre_order(tree[0], tree)
    print()
    in_order(tree[0], tree)
    print()
    post_order(tree[0], tree)