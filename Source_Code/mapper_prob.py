#!/usr/bin/env python
"""mapper.py"""

import sys
def main():
    for line in sys.stdin:
        airline = line.strip().split(',')
        if airline[8]!='UniqueCarrier':
            print('{}\t{}'.format(airline[8],airline[14]))

if __name__ == "__main__":
    main()
