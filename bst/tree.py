
class Tree:

    def __init__(self, root):
        self._root = root


    @property
    def root(self):
        return self._root


    def insert(self, node):
        self.root.insert(node, self.root)


    def delete(self, x):
        node = self.find_node(x, self.root)
        if node != False:
            return self.root.delete(node)
        return False


    def preorder_traverse(self, node):
        if node:
            yield node.val  # preorder
            for v in self.preorder_traverse(node.left_child):
                yield v
            for v in self.preorder_traverse(node.right_child):
                yield v


    def inorder_traverse(self, node):
        if node:
            for v in self.inorder_traverse(node.left_child):
                yield v
            yield node.val  # inorder
            for v in self.inorder_traverse(node.right_child):
                yield v


    def postorder_traverse(self, node):
        if node:
            for v in self.postorder_traverse(node.left_child):
                yield v
            for v in self.postorder_traverse(node.right_child):
                yield v
            yield node.val  # postorder


    def contains(self, x, node):
        if not node:
            return False
        elif x == node.val:
            return True
        elif x < node.val:
            return self.contains(x, node.left_child)
        else:
            return self.contains(x, node.right_child)


    def find_node(self, x, node):
        if not node:
            return False
        elif x == node.val:
            return node
        elif x < node.val:
            return self.find_node(x, node.left_child)
        else:
            return self.find_node(x, node.right_child)


    def find_min(self, node):
        if not node.left_child:
            return node
        else:
            return self.find_min(node.left_child)


    def find_max(self, node):
        if not node.right_child:
            return node
        else:
            return self.find_max(node.right_child)


    def find_smaller(self, x, node):
        if not node:
            pass

        elif node.val >= x:
            for v in self.find_smaller(x, node.left_child):
                yield v
                
        elif node.val < x:
            yield node.val
            for v in self.find_smaller(x, node.left_child):
                yield v
            for v in self.find_smaller(x, node.right_child):
                yield v

    
    def find_bigger(self, x, node):
        if not node:
            pass

        elif node.val <= x:
            for v in self.find_bigger(x, node.right_child):
                yield v

        elif node.val > x:
            yield node.val
            for v in self.find_bigger(x, node.right_child):
                yield v
            for v in self.find_bigger(x, node.left_child):
                yield v

