# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 15:26:22 2020

@author: Soul
"""

arr = []
anss = []

while True:
    n = input()
    if n == "":
        break
    else:
        arr.append(int(n))

for i in arr:
    if i == 42:
        break
    else:
        anss.append(i)

print(*anss, sep='\n')