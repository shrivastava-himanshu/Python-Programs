# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 09:26:59 2018

@author: shrivh1
"""

def prime_generator(n):
    #list primes from 1 to n
    for i in range(1,n,1):
        if prime_check(i):
            print(i)

prime_generator(200)






def prime_check(n):
    flag = 0
    if n > 2 and n % 2 == 0:
        flag = 1
    for i in range(3,n//2,2):
        if n % i == 0:
            flag = 1
    if flag == 0:
        return True
    else:
        return False