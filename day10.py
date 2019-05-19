Task 
Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation.

Input Format

A single integer, .

Constraints

Output Format

Print a single base- integer denoting the maximum number of consecutive 's in the binary representation of .


#################################################################################################################
My Code.......................
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    c=0
    m=0
    while n>0:
        r=n%2
        if r==1:
            c+=1
            if c>m:
                m=c
        else:
            c=0
        n=n//2    
    print(m)               
   
    
