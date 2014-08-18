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
    print('Pre-order traversal:')
    for v in tree.preorder_traverse():
        print(v.val)

    print('In-order traversal:')
    for v in tree.inorder_traverse():
        print(v.val)

    print('Post-order traversal:')
    for v in tree.postorder_traverse():
        print(v.val)

    # Find smallest
    print('Smallest:')
    print(tree.find_min().val)
    
    # Find biggest
    print('Biggest:')
    print(tree.find_max().val)
    
    # Find all smaller than 7
    smaller_than = 7
    print('Smaller than {0}:'.format(smaller_than))
    for v in tree.find_smaller(smaller_than):
        print(v)

    # Find all bigger than 5
    bigger_than = 5
    print('Bigger than {0}'.format(bigger_than))
    for v in tree.find_bigger(bigger_than):
        print(v)

    # Check if tree contains 4
    print('Node 4 exists in tree == {0}'.format(tree.contains(4)))

    # Delete leaf node 18
    print('Node 18 deleted == {0}'.format(tree.delete(18)))


if __name__ == '__main__':
    main()
