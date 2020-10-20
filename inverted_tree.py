

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
# too much work to write tests for this