import sys


class Node:
    def __init__(self, _data, _parent=None):
        self.data = _data
        self.parent = _parent
        self.child = []


class Tree:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, _node):
        _node.parent.child.append(_node)

    def delete(self, _node):
        for child in _node.parent.child:
            if child == _node:
                _node.parent.child.remove(_node)

    def find_leaf(self, _node):
        if _node.child:
            for child in _node.child:
                self.find_leaf(child)
        else:
            self.count += 1


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    input_data = list(map(int, sys.stdin.readline().split()))
    node_list = [Node(data) for data in range(N)]

    tree = Tree()

    for data, parent in enumerate(input_data):
        if parent == -1:
            node_list[data].parent = parent
            tree.root = node_list[data]
        else:
            node_list[data].parent = node_list[parent]
            tree.insert(node_list[data])

    delete_data = int(input())
    if node_list[delete_data].parent == -1:
        print(0)
    else:
        tree.delete(node_list[delete_data])
        tree.find_leaf(tree.root)
        print(tree.count)
