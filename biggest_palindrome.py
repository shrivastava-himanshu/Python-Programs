# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:11:57 2018

@author: shrivh1
"""
#from math import reverse

def big_palindrome():
    l = list(range(100,999))
    outlist = []
    for n in l:
        for m in range(n,999):
            num = n*m
            num1= num
            rev = 0
        
            while(num > 0):
                rem = num %10
                rev = (rev *10) + rem
                num = num // 10
            if num1 == rev:
                
           # print(num1)
                outlist.append(num1)
            else:
                continue
    out = max(outlist)
    print(out)
    

big_palindrome()