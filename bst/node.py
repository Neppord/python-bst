
class Node:

    def __init__(self, val):
        self.parent = None
        self._left_child = None
        self._right_child = None
        self._val = val


    @property
    def left_child(self):
        return self._left_child


    @property
    def right_child(self):
        return self._right_child


    @property
    def val(self):
        return self._val
    

    def insert(self, node, root):
        if not root:
            return False

        elif node.val == root.val:
            return False

        elif node.val < root.val:
            # insert left child
            if not root._left_child:
                root._left_child = node
                node.parent = root
            else:
                self.insert(node, root._left_child)

        else:
            # insert right child
            if not root._right_child:
                root._right_child = node
                node.parent = root
            else:
                self.insert(node, root._right_child)


    def delete(self, node):
        # if node is leaf
        if not node._left_child and not node._right_child:
            if node.parent._left_child is node:
                node.parent._left_child = None
                del node
                return True
            elif node.parent._right_child is node:
                node.parent._right_child = None
                del node
                return True
        else:
            return False

