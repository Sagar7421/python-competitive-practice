# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 00:34:26 2020

@author: Soul
"""
import copy

arr = [[1,0,0,1,1],[0,0,0,0,0],[0,0,0,1,0],[1,0,0,1,0], [1,1,1,1,2]]

quad1, quad2, quad3, quad4 = [], [], [], []

div = len(arr)//2

for i in range(0, div):
    quad1.append(arr[i][:div])
   # print(quad1)
    #print(arr)
                
for j in range(0, div):
    quad2.append(arr[j][div+1:])
    #print(quad2)s

for k in range(0, div):
    quad3.append(arr[k+div+1][:div])

for l in range(0, div):
    quad4.append(arr[l+div+1][div+1:])
    
    
rq2 = []   
rq2.append(quad1[1])

rq2 = copy.deepcopy(quad1)





for p in range(div):
    rq2[p].reverse()

quad2.append(arr[0][div:])