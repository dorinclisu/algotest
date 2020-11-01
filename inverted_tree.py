

def lowest_common_ancestor(node1, node2):
    visited_nodes_set = set()

    while True: # this assumes node1 and node2 belong to the same tree, otherwise this might loop forever
        # go up the 2 tree paths in parallel until they intersect
        if node1: # if node is not root's parent
            if node1 in visited_nodes_set:
                return node1

            visited_nodes_set.add(node1)
            node1 = node1.parent # go up the tree from first node path

        if node2: # if node is not root's parent
            if node2 in visited_nodes_set:
                return node2

            visited_nodes_set.add(node2)
            node2 = node2.parent # go up the tree from second node path


###############################################################################
class Node:
    def __init__(self, parent=None):
        self.parent = parent

#                1
#            2       3
#        6     4    7    5
#            8               9
#         10   11
#                12
n1 = Node()
n2 = Node(n1)
n3 = Node(n1)
n4 = Node(n2)
n5 = Node(n3)
n6 = Node(n2)
n7 = Node(n3)
n8 = Node(n4)
n9 = Node(n5)
n10 = Node(n8)
n11 = Node(n8)
n12 = Node(n11)

assert lowest_common_ancestor(n1, n1) == n1
assert lowest_common_ancestor(n1, n2) == n1
assert lowest_common_ancestor(n2, n3) == n1
assert lowest_common_ancestor(n6, n9) == n1
assert lowest_common_ancestor(n12, n9) == n1
assert lowest_common_ancestor(n6, n8) == n2
assert lowest_common_ancestor(n6, n11) == n2
assert lowest_common_ancestor(n9, n4) == n1
assert lowest_common_ancestor(n9, n7) == n3

print('All good!')
