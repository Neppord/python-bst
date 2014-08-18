#!/usr/bin/env python
import sys, os
from unittest2 import defaultTestLoader, TestSuite, TextTestRunner

def main():
    parent = os.path.dirname(os.path.abspath(__file__))
    if not parent in sys.path:
        sys.path.insert(0, parent)

    # Run tests
    tests = defaultTestLoader.discover('tests')
    suit = TestSuite(tests)
    result = TextTestRunner(verbosity=2, failfast=False).run(suit)


if __name__ == '__main__':
    main()
