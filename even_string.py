# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 13:23:18 2018

@author: shrivh1
"""

def even_string(n):
    final = ''
    for word in n.split():
        if len(word) % 2 == 0:
            mid = int(len(word)/2)
            print(word[:mid])
            final += word[:mid] + ' '
        else:
            print(word)
            final += word + ' '
    print(final)
        
even_string('Hello I am Mike Saunders')