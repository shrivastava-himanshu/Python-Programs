# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 14:52:17 2018

@author: shrivh1
"""

def round10(num):
  r=num%10
#  print(r)
  if r<5:
    num=num - r
  else:
    num=num + (10-r)
#  print(num)
    return num

round10(num)