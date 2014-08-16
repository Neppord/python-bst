#!/usr/bin/env python

from node import Node
from tree import Tree

"""
Python Binary Search Tree Data Structure
    Features:
        * insert
        * delete
        * contains
        * find_min
        * find_max
        * find_smaller
        * pre-order traverse
        * in-order traverse
        * post-order traverse

        Author: Per Magnusson, killingfloor00@gmail.com
        GitHub: https://github.com/permag/python-bst

"""

def main():
    """
    Example usage

    """
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
    tree.preorder_traverse(tree.get_root())

    # Output
    print 'Smallest:'
    print tree.find_min(tree.get_root()).val
    print 'Biggest:'
    print tree.find_max(tree.get_root()).val
    smaller_than = 7
    print 'Smaller than {0}:'.format(smaller_than)
    tree.find_smaller(smaller_than, tree.get_root())
    print tree.contains(4, tree.get_root())

    # tree.delete(18)
    # tree.preorder_traverse(tree.get_root())


if __name__ == '__main__':
    main()
