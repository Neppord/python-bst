#!/usr/bin/env python

from bst import Node, Tree

"""
Python Binary Search Tree Data Structure
    Features:
        * insert
        * delete
        * contains
        * find_min
        * find_max
        * find_smaller
        * pre-order traversal
        * in-order traversal
        * post-order traversal

        Author: Per Magnusson, killingfloor00@gmail.com
        GitHub: https://github.com/permag/python-bst

"""

def main():
    """
    Example usage

    """

    # Insert nodes in tree
    tree = Tree(Node(9))
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
    print 'Pre-order traversal'
    for v in tree.preorder_traverse(tree.root):
        print v

    # Find smallest
    print 'Smallest:'
    print tree.find_min(tree.root).val
    
    # Find biggest
    print 'Biggest:'
    print tree.find_max(tree.root).val
    
    # Find all smaller than 7
    smaller_than = 7
    print 'Smaller than {0}:'.format(smaller_than)
    for v in tree.find_smaller(smaller_than, tree.root):
        print v

    # Check if tree contains 4
    print tree.contains(4, tree.root)

    # tree.delete(18)


if __name__ == '__main__':
    main()

