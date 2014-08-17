
class Node:

    def __init__(self, val):
        self.parent = None
        self._left_child = None
        self._right_child = None
        self._val = val


    @property
    def left_child(self):
        return self._left_child


    @left_child.setter
    def left_child(self, value):
        self._left_child = value


    @property
    def right_child(self):
        return self._right_child


    @right_child.setter
    def right_child(self, value):
        self._right_child = value


    @property
    def val(self):
        return self._val


    @val.setter
    def val(self, value):
        self._val = value
    

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

