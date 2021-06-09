# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 14:28:46 2020

@author: Soul
"""

for _ in range(int(input())):
    N = int(input())
    dishes = list(map(int, input().split()))
    times = 0
    if N == 4:
        dishes.sort()
        times = dishes[1] + dishes[2]
        print(times)
    elif N == 3:
        dishes.sort()
        times = dishes[0] + dishes[1]
        print(times)
    else:
        times = sum(dishes)
        print(times)
        