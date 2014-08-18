#!/usr/bin/env python
from bst import Node, Tree

"""
Python Binary Search Tree Data Structure
    Features:
        * insert
        * delete
        * contains
        * find_node
        * find_min
        * find_max
        * find_smaller
        * find_bigger
        * pre-order traversal
        * in-order traversal
        * post-order traversal

        Author: Per Magnusson, perm00@me.com
        GitHub: https://github.com/permag/python-bst

"""

def main():
    """ Example usage """

    # Insert nodes in tree
    tree = Tree(Node(9))  # root node
    tree.insert(Node(6))
    tree.insert(Node(22))
    tree.insert(Node(1))
    tree.insert(Node(4))
    tree.insert(Node(2))
    tree.insert(Node(18))

    """
    Tree after above insertion:
         9
       /   \
      6     22
     /      / 
    1      18
     \
      4
     /
    2

    """

    # Traverse tree
    print('Pre-order traversal:'),
    print(', '.join(str(node.val) for node in  tree.preorder_traverse()))

    print('\nIn-order traversal:'),
    print(', '.join(str(node.val) for node in tree.inorder_traverse()))

    print('\nPost-order traversal:'),
    print(', '.join(str(node.val) for node in tree.postorder_traverse()))

    # Find smallest
    print('\nSmallest:'),
    print(tree.find_min().val)
    
    # Find biggest
    print('\nBiggest:'),
    print(tree.find_max().val)
    
    # Find all smaller than 7
    smaller_than = 7
    print('\nSmaller than {0}:'.format(smaller_than)),
    print(', '.join(str(node.val) for node in tree.find_smaller(smaller_than)))

    # Find all bigger than 5
    bigger_than = 5
    print('\nBigger than {0}:'.format(bigger_than)),
    print(', '.join(str(node.val) for node in tree.find_bigger(bigger_than)))

    # Check if tree contains 4
    contains = 4
    print('\nNode {0} exists in tree == {1}'.format(contains, tree.contains(contains)))

    # Delete leaf node 18
    delete = 18
    print('\nNode {0} was deleted == {1}'.format(delete, tree.delete(delete)))


if __name__ == '__main__':
    main()
