#!/usr/bin/env python
import sys, os
from unittest2 import defaultTestLoader as TestLoader, TestSuite, TextTestRunner as TestRunner

def main():
    parent = os.path.dirname(os.path.abspath(__file__))
    if not parent in sys.path:
        sys.path.insert(0, parent)

    # Run tests
    tests = TestLoader.discover('tests')
    suit = TestSuite(tests)
    result = TestRunner(verbosity=1, failfast=False).run(suit)
    exit_code = len(result.failures) + len(result.errors)

    sys.exit(exit_code)


if __name__ == '__main__':
    main()
