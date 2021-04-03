#!/usr/bin/env python
"""reducer.py"""

import sys
def main():
    finallist = []
    totalDelay = 0
    oldKey = None
    count = 0
    
    infile = sys.stdin
    
    for line in infile:

        data_mapped=line.strip().split('\t')

        if data_mapped[1]!='NA':
            thisKey, arrDelay = data_mapped[0],int(data_mapped[1])
    
            if oldKey and oldKey != thisKey:
                finallist.append((oldKey,1-(totalDelay/count)))
                oldKey = thisKey;
                totalDelay = 0
                count = 0

            oldKey = thisKey
            count += 1
            if arrDelay>0:
                totalDelay += 1

    if oldKey != None:
        finallist.append((oldKey,1-(totalDelay/count)))

    def Sort(sub_li):
        return(sorted(sub_li, key = lambda x: x[1])) 

    top3 = (Sort(finallist)[0:3])
    print('3 Airlines with Lowest Prob to be on Schedule')
    for i in top3:
        print(i[0],i[1])

    bottom3=sorted(Sort(finallist)[-3:],key = lambda x: x[1],reverse=True)
    print('3 Airlines with Highest Prob to be on Schedule')
    for i in bottom3:
        print(i[0],i[1])


if __name__=='__main__':
    main()
