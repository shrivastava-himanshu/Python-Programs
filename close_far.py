# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 17:14:21 2018

@author: shrivh1
"""

def close_far(a, b, c):
  if abs(a-b)<=1 and abs(a-c)>=2:
      print (a-b)
      print (a-c)
      print('True')
  elif abs(a-c)<=1 and abs(a-b)>=2:
      print (a-b)
      print (a-c)
      print('True')
  else:
      print (a-b)
      print (a-c)
      print('False')


close_far(10,8,9)

