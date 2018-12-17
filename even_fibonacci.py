# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 22:20:31 2018

@author: shrivh1
"""

def even_fibonacci():
    a = 1
    b = 2
    sum1 = 0
    while (a <= 4000000):
        if a % 2 == 0:
            sum1 += a
        a,b = b,a+b


    print(sum1)
#    if n %2 == 0:
#        sum = sum + n
#    print(sum)
#        
even_fibonacci()