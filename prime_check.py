# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 09:21:05 2018

@author: shrivh1
"""

def prime_check(n):
    flag = 0
    if n > 2 and n % 2 == 0:
        flag = 1
    for i in range(3,n//2,2):
        if n % i == 0:
            flag = 1
    if flag == 0:
        print('Prime')
    else:
        print('Not Prime')

prime_check(108)