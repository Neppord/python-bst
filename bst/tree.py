
class Tree:

    def __init__(self, root):
        self._root = root


    @property
    def root(self):
        return self._root


    def insert(self, node):
        self.root.insert(node, self.root)


    def delete(self, x):
        node = self.find_node(x)
        if node != False:
            return self.root.delete(node)
        return False


    def preorder_traverse(self):
        return self.root.preorder_traverse()


    def inorder_traverse(self):
        def traverse(node):
            if node:
                for v in traverse(node.left_child):
                    yield v
                yield node  # inorder
                for v in traverse(node.right_child):
                    yield v

        return traverse(self.root)


    def postorder_traverse(self):
        def traverse(node):
            if node:
                for v in traverse(node.left_child):
                    yield v
                for v in traverse(node.right_child):
                    yield v
                yield node  # postorder

        return traverse(self.root)


    def contains(self, x):
        def cont(x, node):
            if not node:
                return False
            elif x == node.val:
                return True
            elif x < node.val:
                return cont(x, node.left_child)
            else:
                return cont(x, node.right_child)

        return cont(x, self.root)


    def find_node(self, x):
        def find(x, node):
            if not node:
                return False
            elif x == node.val:
                return node
            elif x < node.val:
                return find(x, node.left_child)
            else:
                return find(x, node.right_child)

        return find(x, self.root)


    def find_min(self):
        def find(node):
            if not node.left_child:
                return node
            else:
                return find(node.left_child)

        return find(self.root)


    def find_max(self):
        def find(node):
            if not node.right_child:
                return node
            else:
                return find(node.right_child)

        return find(self.root)


    def find_smaller(self, x):
        def find(x, node):
            if not node:
                pass

            elif node.val >= x:
                for v in find(x, node.left_child):
                    yield v
                    
            elif node.val < x:
                yield node
                for v in find(x, node.left_child):
                    yield v
                for v in find(x, node.right_child):
                    yield v

        return find(x, self.root)


    def find_bigger(self, x):
        def find(x, node):
            if not node:
                pass

            elif node.val <= x:
                for v in find(x, node.right_child):
                    yield v

            elif node.val > x:
                yield node
                for v in find(x, node.right_child):
                    yield v
                for v in find(x, node.left_child):
                    yield v

        return find(x, self.root)

