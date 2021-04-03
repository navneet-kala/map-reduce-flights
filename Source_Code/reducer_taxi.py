#!/usr/bin/env python
"""reducer.py"""

import sys
import re

def main():
    finallist_IN = []
    finallist_OUT = []

    totalTaxi = 0
    oldKey = None
    count = 0
    infile = sys.stdin

    
    for line in infile:

        data_mapped=line.strip().split('\t')

        if data_mapped[1]!='NA':
            thisKey, taxi = data_mapped[0],int(data_mapped[1])
            if oldKey and oldKey != thisKey:
                if oldKey.split('-')[1]=='IN':
                    finallist_IN.append((oldKey.split('-')[0],totalTaxi/count))
                else:
                    finallist_OUT.append((oldKey.split('-')[0],totalTaxi/count))
                oldKey = thisKey;
                totalTaxi = 0
                count = 0

            oldKey = thisKey
        
            count += 1
            totalTaxi += taxi
        

    if oldKey != None:
        if oldKey.split('-')[1]=='IN':
            finallist_IN.append((oldKey.split('-')[0],totalTaxi/count))
        else:
            finallist_OUT.append((oldKey.split('-')[0],totalTaxi/count))

    def Sort(sub_li):
        return(sorted(sub_li, key = lambda x: x[1])) 

    top3_IN = (Sort(finallist_IN)[0:3])
    print('3 Airports with Lowest average taxi IN times')
    for i in top3_IN:
        print(i[0],i[1])

    bottom3_IN=sorted(Sort(finallist_IN)[-3:],key = lambda x: x[1],reverse=True)
    print('3 Airports with Highest average taxi IN times')
    for i in bottom3_IN:
        print(i[0],i[1])

    top3_OUT = (Sort(finallist_OUT)[0:3])
    print('3 Airports with Lowest average taxi OUT times')
    for i in top3_OUT:
        print(i[0],i[1])

    bottom3_OUT=sorted(Sort(finallist_OUT)[-3:],key = lambda x: x[1],reverse=True)
    print('3 Airports with Highest average taxi OUT times')
    for i in bottom3_OUT:
        print(i[0],i[1])


if __name__=='__main__':
    main()
