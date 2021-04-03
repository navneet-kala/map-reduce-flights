#!/usr/bin/env python
"""reducer.py"""

import sys
def main():
    finallist = []
    oldKey = None
    count = 0
    
    infile = sys.stdin
    
    for line in infile:

        data_mapped=line.strip().split('\t')

        if data_mapped[0]!='NA':
            if data_mapped[0] == 'A':
                thisKey = 'Carrier'
            elif data_mapped[0] == 'B':
                thisKey = 'Weather'
            elif data_mapped[0] == 'C':
                thisKey = 'NAS'
            elif data_mapped[0] == 'D':
                thisKey = 'Security'
            else:
                continue
    
            if oldKey and oldKey != thisKey:
                finallist.append((oldKey,count))
                oldKey = thisKey;
                count = 0

            oldKey = thisKey
            count += 1

    if oldKey != None:
        finallist.append((oldKey,count))

    def Sort(sub_li):
        return(sorted(sub_li, key = lambda x: x[1])) 


    bottom3=sorted(Sort(finallist)[:],key = lambda x: x[1],reverse=True)
    print('Most Common Reason for Cancellation in Descending Order')
    for i in bottom3:
        print(i[0],i[1])


if __name__=='__main__':
    main()
