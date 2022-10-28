#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    count=0
    for j in range(n):
        swap= False
        for i in range(0,n-1-j):
            if(a[i]>a[i+1]):
                x=a[i]
                y=a[i+1]
                a[i]=y
                a[i+1]=x 
                swap=True
                count=count+1
            
        if(swap==False):
            break;
        j=j+1
    print("Array is sorted in "+str(count)+" swaps.")
    print("First Element: "+str(a[0]))
    print("Last Element: "+str(a[-1]))

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
