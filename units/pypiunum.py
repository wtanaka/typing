#!/usr/bin/env python
"""Evaluation of https://pypi.python.org/pypi/Unum/4.1.3
"""
import sys

import unum.units

def main():
    """Main function"""
    print "sys.getsizeof = {} compared to {} for a float".format(
        sys.getsizeof(5.0 * unum.units.m), sys.getsizeof(5.0))
    print type(5.0 * unum.units.m)

if __name__ == "__main__":
    main()
