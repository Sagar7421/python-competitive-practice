# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 19:30:38 2020

@author: Soul
"""

def revs(a):
    a = a[::-1]
    return int(a)

res = []

for _ in range(int(input())):
    nums = input()
    res.append(revs(nums))
    

print(*res, sep='\n')