
class Node:
    def __init__(self, val):
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.val = val


    def insert(self, node, root):
        if not root:
            return False

        elif node.val == root.val:
            return False

        elif node.val < root.val:
            # insert left child
            if not root.left_child:
                root.left_child = node
                node.parent = root
            else:
                self.insert(node, root.left_child)
        else:
            # insert right child
            if not root.right_child:
                root.right_child = node
                node.parent = root
            else:
                self.insert(node, root.right_child)


    def delete(self, node):
        # if node is leaf
        if not node.left_child and not node.right_child:
            if node.parent.left_child is node:
                node.parent.left_child = None
                del node
            elif node.parent.right_child is node:
                node.parent.right_child = None
                del node

