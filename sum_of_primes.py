# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 22:40:03 2018

@author: shrivh1
"""




def sum_of_primes(n):
    #list primes from 1 to n
    s = 0
    for i in range(1,n,1):
        if prime_check(i):
            s += i
    print(s)
    
sum_of_primes(18)






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

#def sum_of_primes(n):
#    s = -1
#    for i in range(1,n,1):
#        flag = 0
#        for j in range(2,i,1):
#            if i % j == 0:
#                flag = 1
#                break
#        if flag == 0:
#            s+=i
#    print(str(s))
#    
    
#    s = 2
#    for i in range(17,2,-1):
#        for j in range(1, i//2,1):
#            if i % j == 0:
#                print('non ' + str(i))
#                break
#            else:
#                print('prime ' + str(i))
#            s += i
#    #print(s)
    

sum_of_primes(2000000)