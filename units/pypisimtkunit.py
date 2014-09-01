#!/usr/bin/env python
"""Evaluation of https://pypi.python.org/pypi/simtk.unit
"""
import sys

import simtk.unit

def main():
    """Main function"""
    print "sys.getsizeof = {} compared to {} for a float".format(
        sys.getsizeof(5.0 * simtk.unit.meter), sys.getsizeof(5.0))
    print type(5.0 * simtk.unit.meter)

if __name__ == "__main__":
    main()
