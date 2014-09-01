#!/usr/bin/env python
"""Evaluation of http://dirac.cnrs-orleans.fr/ScientificPython
"""
import sys

import Scientific.Physics.PhysicalQuantities

def main():
    """Main function"""
    fivemeter = Scientific.Physics.PhysicalQuantities.PhysicalQuantity(
        5.0, 'm')
    print "sys.getsizeof = {} compared to {} for a float".format(
        sys.getsizeof(fivemeter), sys.getsizeof(5.0))

if __name__ == "__main__":
    main()
