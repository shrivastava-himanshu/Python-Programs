# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 14:58:18 2018

@author: shrivh1
"""

def make_bricks(small, big, goal):
  if goal > small + big * 5:
    print ('False')
  else:
    print ( goal % 5 <= small)

make_bricks(1,2,3)