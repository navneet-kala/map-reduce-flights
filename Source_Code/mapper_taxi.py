#!/usr/bin/env python
"""mapper.py"""
import sys
def main():
    for line in sys.stdin:
        airline = line.strip().split(',')
        if airline[8]!='UniqueCarrier':
            if airline[20]!='0':
                print('{}\t{}'.format(airline[16]+'-'+'OUT',airline[20]))
            if airline[19]!='0':
                print('{}\t{}'.format(airline[17]+'-'+'IN',airline[19]))
    

if __name__ == "__main__":
    main()

