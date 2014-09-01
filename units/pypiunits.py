#!/usr/bin/env python
"""Evaluation of https://pypi.python.org/pypi/units/
"""
import sys

import units
import units.predefined

def main():
    """Main function"""
    units.predefined.define_units()
    meter = units.unit('m')
    print "sys.getsizeof = {} compared to {} for a float".format(
        sys.getsizeof(meter(5.0)), sys.getsizeof(5.0))

if __name__ == "__main__":
    main()
