# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 22:19:37 2018

@author: shrivh1
"""

def sum_of_squares():
    sum_of_sq = 0
    sum_of_num= 0
    list1 = [1,2,3,4,5,6,7,8,9,10]
    for i in list1:
        sum_of_sq += int(i*i)
    for j in list1:
        sum_of_num += int(j)
    diff = int(sum_of_squares - (sum_of_num*sum_of_num))
    print(diff)


sum_of_squares()