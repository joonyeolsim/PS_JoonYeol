def binary_search(sub_tree, _k, _tree_dict):
    mid_index = len(sub_tree) // 2
    tree_dict[_k].append(sub_tree[mid_index])
    if _k > 1:
        _k -= 1
        binary_search(sub_tree[0:mid_index], _k, _tree_dict)
        binary_search(sub_tree[mid_index+1:], _k, _tree_dict)


if __name__ == '__main__':
    k = int(input())
    tree_dict = dict()
    tree = list(map(int, input().split()))
    for i in range(1, k+1):
        tree_dict[i] = list()
    binary_search(tree, k, tree_dict)

    for i in range(k, 0, -1):
        print(*tree_dict[i], sep=' ')