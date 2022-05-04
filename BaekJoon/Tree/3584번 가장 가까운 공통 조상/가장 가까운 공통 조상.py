import sys


class Node:
    def __init__(self, _node):
        self.parent = None
        self.ancestor_list = []
        self.node = _node

    def get_ancestors(self):
        this_node = self
        self.ancestor_list.append(this_node)
        while this_node.parent:
            self.ancestor_list.append(this_node.parent)
            this_node = this_node.parent
        return self.ancestor_list

    def __eq__(self, other):
        return self.node == other.node


if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        node_num = int(sys.stdin.readline().strip())
        node_list = [Node(i) for i in range(node_num + 1)]
        for _ in range(node_num - 1):
            parent, child = map(int, sys.stdin.readline().split())
            node_list[child].parent = node_list[parent]

        node1, node2 = map(int, sys.stdin.readline().split())
        node1_ancestor_list = node_list[node1].get_ancestors()
        node2_ancestor_list = node_list[node2].get_ancestors()

        min_ancestor_node = -1
        min_ancestor_depth = node_num
        for i, ancestor_node1 in enumerate(node1_ancestor_list):
            for j, ancestor_node2 in enumerate(node2_ancestor_list):
                if ancestor_node1 == ancestor_node2 and min_ancestor_depth > min(i, j):
                    min_ancestor_depth = min(i, j)
                    min_ancestor_node = ancestor_node1
        print(min_ancestor_node.node)