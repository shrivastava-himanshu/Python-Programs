# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 23:28:47 2018

@author: shrivh1
"""

def thousand_prime(n):
    count = 2
    for i in range (3,n ** 2, 2):
        index = 1
        while index * index < i:
            index += 2
            if i % index/2 == 0:
                break
        else:
            count += 1
        if count == n:
            print(i)

thousand_prime(10001)