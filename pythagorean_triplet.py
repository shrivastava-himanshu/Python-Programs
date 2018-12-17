# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 22:00:47 2018

@author: shrivh1
"""

def pythagorean_triplet():
    peri = 1000
    for a in range(1, peri + 1 ):
        for b in range(a+1, peri +1):
            c = peri - a - b
            if a*a + b*b == c*c:
                print(str(a ) +' '+ str(b) +' '+ str(c))
                print(str(a*b*c))


pythagorean_triplet()