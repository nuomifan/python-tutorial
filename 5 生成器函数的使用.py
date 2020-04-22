# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:24:36 2020

@author: demon
"""

'''
def createlist():
    mylist = [x for x in range(10000)]
    return mylist


print(createlist())
'''

def createlist():
    for i in range(100):
        print(i)
        yield i


x = createlist()

next(x)
next(x) 
next(x)

