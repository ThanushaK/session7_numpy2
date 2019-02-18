# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 19:20:04 2019

@author: thanusha
"""

import numpy as np  #imported numpy library 
b=[3,5,7,2,8,10,11,65,72,81,99,100,150]  #test input
def moving_average(a, n) : #defining function
    ret = np.cumsum(a) #calculating cummulative sum
    #print(ret)
    #print(ret[n:])
    #print(ret[:-n])
    ret[n:] = ret[n:] - ret[:-n]  #calculating the sum in a given window size n
    #print(ret[n:])
    #print(ret[n - 1:])
    return ret[n - 1:] / n #return the result
print(moving_average(b,3)) # function call and printing the result

