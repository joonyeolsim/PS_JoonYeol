import sys


class Node:
    def __init__(self, element, parent):
        self.element = element
        self.parent = parent
        self.children = []


class Tree:
    def __init__(self, root_element):
        self.root = Node(root_element, None)
        self.node_list = [self.root]

    def insert(self, parent_element, child_element):
        parent_node = self.find(parent_element)
        child_node = Node(child_element, parent_node)
        parent_node.children.append(child_node)
        self.node_list.append(child_node)

    def find(self, element):
        for node_ in self.node_list:
            if node_.element == element:
                return node_
        return None

    def get_depth(self, node_):
        depth = 0
        while node_.parent:
            depth += 1
            node_ = node_.parent
        return depth


def get_continuous_list(pointer_, num_list_):
    last_num = num_list_[pointer_]
    continuous_list = [last_num]

    for num in num_list_[pointer_ + 1:]:
        if num == last_num + 1:
            continuous_list.append(num)
            last_num = num
        else:
            break
    return continuous_list


if __name__ == '__main__':
    while True:
        n, k = map(int, sys.stdin.readline().split())
        if n == 0 and k == 0:
            break

        num_list = list(map(int, sys.stdin.readline().split()))

        root_num = num_list[0]
        tree = Tree(num_list[0])
        parent_list = [root_num]

        pointer = 1
        while pointer < n:
            child_list = get_continuous_list(pointer, num_list)
            pointer = pointer + len(child_list)
            parent = parent_list.pop(0)
            for child in child_list:
                tree.insert(parent, child)
            parent_list.extend(child_list)

        k_node = tree.find(k)
        k_depth = tree.get_depth(k_node)
        siblings = 0
        for node in tree.node_list:
            if k_depth == tree.get_depth(node) and node.parent != k_node.parent and node.parent.parent == k_node.parent.parent:
                siblings += 1

        print(siblings)
