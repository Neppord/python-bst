from itertools import chain

class Node:

    def __init__(self, val):
        self._parent = None
        self._left_child = None
        self._right_child = None
        self._val = val


    @property
    def parent(self):
        return self._parent
    

    @property
    def left_child(self):
        return self._left_child


    @property
    def right_child(self):
        return self._right_child


    @property
    def val(self):
        return self._val
    
    def preorder_traverse(self):
        left = self._preorder_traverse_left()
        right = self._preorder_traverse_right()
        return chain((self,), left, right)

    def _preorder_traverse_left(self):
        if self.left_child:
            return self.left_child.preorder_traverse()
        else:
            return ()

    def _preorder_traverse_right(self):
        if self.right_child:
            return self.right_child.preorder_traverse()
        else:
            return ()
        

    

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

