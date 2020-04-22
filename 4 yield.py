# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:18:12 2020

@author: demon
"""
def go():
    print(1)
    print(2)
    print(3)

def goX():
    print(1)
    yield 10
    print(2)
    yield 20
    print(3)
    yield 30
    print(4)
    yield 40

# print(type(go))
# print(type(go()))
# print(type(goX))
# print(type(goX()))

X = goX()

print(next(X))
print(next(X))
print(next(X))
print(next(X))