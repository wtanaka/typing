#!/usr/bin/env python
"""Evaluation of https://pypi.python.org/pypi/quantities/
"""
import sys

import quantities

def main():
    """Main function"""
    onejoule = quantities.Quantity([1.0], quantities.J)
    print "sys.getsizeof = {} compared to {} for a float".format(
        sys.getsizeof(onejoule), sys.getsizeof(1.0))

if __name__ == "__main__":
    main()
